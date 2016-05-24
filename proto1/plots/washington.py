import hashlib
import json
import logging
import math

import constance
from django.conf import settings
from django.core.cache import cache
from scipy.interpolate import interp1d

from proto1 import defaults, constants
from proto1 import util
from proto1.models import ExpectedFamilyContributionModel, PellGrantModel, InstitutionModel, StateAppropriationModel, \
    EnrollmentModel, PovertyGuidelineModel, GrantsScholarshipsModel, AffordableDebtModel
from proto1.plots.base_plot import BasePlot
from proto1.plots.common_utils import fetch_min_wage, compute_time_to_graduate
from proto1.plots.compress import Smoothen
from proto1.scenario import KEY_STATE_NEED_GRANT_MAX_AWARD, \
    KEY_STATE_NEED_GRANT_DISTRIBUTION_SCHEDULE
from proto1.transform import import_poverty_guideline, import_state_need_grant_max_award, \
    import_state_need_grant_distribution_schedule, compute_interest, compute_cost_of_attendance, \
    compute_median_family_income

__author__ = 'gautam'


# TODO Implement an error handler. Instead of copping out when something goes wrong, display the error on the screen

class FamilyIncomePlot(BasePlot):
    def __init__(self):
        super(FamilyIncomePlot, self).__init__()
        self.discretionary_income_contribution = None
        self.poverty_guideline = None
        self.median_family = None

    def plot(self):
        data_points = []
        for percent_mfi in xrange(1, 201):
            income = (self.median_family_income * percent_mfi / 100)
            disc_income = income - self.basic_necessities
            if disc_income < 0:
                contribution = 0
            else:
                contribution = math.floor(disc_income * self.discretionary_income_contribution)
            data_points.append(contribution)
        return data_points

    def _basic_necessities(self):
        q_poverty_guideline = PovertyGuidelineModel.objects.get(year=self.year)
        return q_poverty_guideline.first_person + (self.family_size - 1) * q_poverty_guideline.each_additional_person

    def set_up(self, scenario):
        super(FamilyIncomePlot, self).set_up(scenario)
        self.family_size = scenario.get(constants.FAMILY_SIZE, defaults.DEFAULT_FAMILY_SIZE)
        self.fie_threshold = float(scenario.get(constants.FIE_THRESHOLD,
                                                defaults.DEFAULT_FIE_THRESHOLD))
        self.state = scenario.get(constants.STATE, defaults.DEFAULT_STATE)
        self.year = scenario.get(constants.CALENDAR_YEAR)

        self.discretionary_income_contribution = float(scenario.get(constants.DISC_INCOME_CONTRIBUTION)) / 100
        self.median_family_income = compute_median_family_income(scenario)
        self.basic_necessities = self._basic_necessities() * self.fie_threshold / 100

    def compute(self, scenario):
        """
        :type scenario: Scenario
        :param scenario:
        :return:
        """
        self.set_up(scenario)
        plot_data = self.plot()
        return {
            constants.TYPE: constants.POINTS,
            constants.DATA: plot_data
        }


class CollegeSavingsPlot(BasePlot):
    """
        Money saved for College by the student's family

        :param str institution_type:
        :param int family_size:
        :param float family_income_exclusion_threshold:
        :param str state:
        :param int year:
        :param float years_of_savings:
        :param float percent_discretionary_income_saved:
        :param float interest_earned:

    """

    def __init__(self):
        super(CollegeSavingsPlot, self).__init__()
        self.poverty_guideline = None
        self.median_family = None
        self.years_of_savings = None
        self.percent_discretionary_income_saved = None
        self.discretionary_incomes = None

    def set_up(self, scenario):
        """
        Fetch all the required parameters from scenario.
        `self.median_family_income` is computed using :py:func:`.compute_median_family_income`


        :param scenario:
        :return:
        """
        super(CollegeSavingsPlot, self).set_up(scenario)
        self.institution_type = scenario.get(constants.INSTITUTION_TYPE)
        self.family_size = scenario.get(constants.FAMILY_SIZE, defaults.DEFAULT_FAMILY_SIZE)
        self.fie_threshold = float(scenario.get(constants.FIE_THRESHOLD,
                                                defaults.DEFAULT_FIE_THRESHOLD))
        self.state = scenario.get(constants.STATE, defaults.DEFAULT_STATE)
        self.year = scenario.get(constants.CALENDAR_YEAR)

        self.time_to_graduate = compute_time_to_graduate(scenario)
        self.years_of_savings = float(scenario.get(constants.YEARS_OF_SAVING))
        self.percent_discretionary_income_saved = float(scenario.get(constants.PERCENT_DISC_INCOME_SAVED)) / 100
        self.interest_earned = float(scenario.get(constants.INTEREST_EARNED))

        self.median_family_income = compute_median_family_income(scenario)
        self.basic_necessities = self._basic_necessities() * self.fie_threshold / 100

    def _basic_necessities(self):
        q_poverty_guideline = PovertyGuidelineModel.objects.get(year=self.year)
        return q_poverty_guideline.first_person + (self.family_size - 1) * q_poverty_guideline.each_additional_person

    def plot(self):
        """
        Generate the data points for the plot.

        * For :math:`\lim_{1 -> 200}` percent_median_family_income
            - `income = median_family_income * percent_median_family_income`
            - `disc_income = income - basic_necessities`
            - proceed `if disc_income > 0`
            - `annual_deposit = disc_income * percent_disc_income_saved`
            - `total_savings =` :py:func:`.compute_interest`

        :return:
        """
        data_points = []
        for percent_mfi in xrange(1, 201):
            income = float(self.median_family_income * percent_mfi / 100)
            disc_income = income - self.basic_necessities
            if disc_income > 0:
                annual_deposit = disc_income * self.percent_discretionary_income_saved
                total_savings = compute_interest(annual_deposit,
                                                 self.interest_earned / 100,
                                                 self.years_of_savings,
                                                 self.time_to_graduate)
                savings = math.floor(total_savings)
            else:
                savings = 0
            if self.institution_type == constants.DB_REF_COMMUNITY_COLLEGES:
                savings *= constance.config.COMMUNITY_COLLEGE_PRO_RATION
            data_points.append(savings)

        return data_points

    def compute(self, scenario):
        """

        :param scenario:
        :return:
        """

        self.set_up(scenario)
        plot_data = self.plot()
        return {
            constants.TYPE: constants.POINTS,
            constants.DATA: plot_data
        }


class StateNeedGrantPlot(BasePlot):
    def __init__(self):
        super(StateNeedGrantPlot, self).__init__()
        self.sng_max_award = None
        self.distribution_schedule = None

    def adjust_sng_with_tuition(self, sng_iterable):
        for sng in sng_iterable:
            constant = self.unadjusted_coa[constants.TUITION] + sng
            new_val = constant - self.adjusted_coa[constants.TUITION]
            yield 0 if sng <= 0 else new_val

    def plot(self):
        data_points = []
        for percent_of_median_income in xrange(1, 201):
            for schedule in self.distribution_schedule:
                lower = schedule[0]
                upper = schedule[1]
                percent_of_max = schedule[2]
                if lower <= percent_of_median_income <= upper:
                    data_points.append(self.sng_max_award * percent_of_max)
        data_points += [0 for x in xrange(1, 201 - len(data_points))]
        return list(self.adjust_sng_with_tuition(data_points))

    def set_up(self, scenario):
        self.time_to_graduate = compute_time_to_graduate(scenario)
        import_state_need_grant_max_award(scenario)
        import_state_need_grant_distribution_schedule(scenario)
        self.sng_max_award = scenario.get(KEY_STATE_NEED_GRANT_MAX_AWARD)[0].sng_max_award
        self.distribution_schedule = [(schedule.percent_mfi_lower,
                                       schedule.percent_mfi_upper,
                                       schedule.percent_of_max_award) for schedule in
                                      scenario.get(KEY_STATE_NEED_GRANT_DISTRIBUTION_SCHEDULE)]

        self.institution_type = scenario.get(constants.INSTITUTION_TYPE)
        self.state = scenario.get(constants.STATE)
        self.calendar_year = scenario.get(constants.CALENDAR_YEAR)
        self.living_status = scenario.get(constants.LIVING_STATUS)
        self.tuition_adjustment = float(scenario.get(constants.TUITION_ADJUSTMENT))
        self.unadjusted_coa = compute_cost_of_attendance(year=self.calendar_year,
                                                         institution_type=self.institution_type,
                                                         state=self.state,
                                                         living_status=self.living_status)
        self.adjusted_coa = compute_cost_of_attendance(year=self.calendar_year,
                                                       institution_type=self.institution_type,
                                                       state=self.state,
                                                       living_status=self.living_status,
                                                       tuition_cost_adjustment=self.tuition_adjustment)

    def compute(self, scenario):
        self.set_up(scenario)
        plot_data = self.plot()
        smooth = constance.config.ENABLE_PLOT_SMOOTH_SWITCH and scenario.get(constants.PLOT_SMOOTHING)
        result = Smoothen().compress(plot_data) if smooth else plot_data
        return {
            constants.TYPE: constants.POINTS,
            constants.DATA: result
        }


class PellGrantPlot(BasePlot):
    def compute_expected_family_contribution(self, income):
        efc = math.floor(0.31 * income - 14420.03)
        return efc if efc > 0 else 0

    def plot(self):
        data_points = []
        coa = self.cost_of_attendance
        pell_for_coa = filter(lambda x1: x1.coa_lower <= coa <= x1.coa_upper, self.pell_grants)
        for percent_of_median_income in xrange(1, 201):
            income = float(self.median_family_income) * percent_of_median_income / 100
            efc = self.compute_expected_family_contribution(income)
            matching_pell = filter(
                lambda x1: x1.efc_lower <= efc <= x1.efc_upper, pell_for_coa)
            data_points += [x.pell_award for x in matching_pell]
        return data_points

    def __init__(self):
        self.academic_year = None
        self.time_to_graduate = None
        self.state = None
        self.living_status = None
        self.institution_type = None
        self.tuition_cost_adjustment = None

    def __hash__(self):
        return hashlib.md5(json.dumps({
            constants.ACADEMIC_YEAR: self.academic_year,
            constants.TIME_TO_GRADUATE: self.time_to_graduate,
            constants.STATE: self.state,
            constants.LIVING_STATUS: self.living_status,
            constants.INSTITUTION_TYPE: self.institution_type,
            'computation_name': 'pellgrant_plot'
        })).hexdigest()

    def set_up_signature(self, scenario):
        self.academic_year = scenario.get(constants.CALENDAR_YEAR)
        self.time_to_graduate = compute_time_to_graduate(scenario)
        self.state = scenario.get(constants.STATE)
        self.living_status = scenario.get(constants.LIVING_STATUS)
        self.institution_type = scenario.get(constants.INSTITUTION_TYPE)
        self.tuition_cost_adjustment = float(scenario.get(constants.TUITION_ADJUSTMENT))

    def set_up(self, scenario):
        import_poverty_guideline(scenario)

        coa = compute_cost_of_attendance(
            year=self.academic_year,
            state=self.state,
            living_status=self.living_status,
            institution_type=self.institution_type,
            tuition_cost_adjustment=self.tuition_cost_adjustment
        )
        self.cost_of_attendance = coa[constants.TUITION] + coa[constants.NON_TUITION]
        self.median_family_income = compute_median_family_income(scenario)
        self.pell_grants = list(PellGrantModel.objects.filter(academic_year=self.academic_year))
        self.expected_family_contributions = list(ExpectedFamilyContributionModel.objects.all())

    def compute(self, scenario):
        self.set_up_signature(scenario)
        cache_key = self.__hash__()
        plot_data = cache.get(cache_key)
        if not plot_data:
            self.set_up(scenario)
            plot_data = self.plot()
            cache.set(cache_key, plot_data, settings.CACHE_LENGTH)
        return {
            constants.TYPE: constants.POINTS,
            constants.DATA: plot_data
        }


class MinimumWagePlot(BasePlot):
    def __init__(self):
        self.hours_worked = None
        self.calendar_year = None
        self.state = None
        self.min_wage = 1

    def compute(self, scenario):
        self.set_up(scenario)
        wage = self.min_wage * self.hours_worked
        take_home_pay = wage * defaults.PERCENT_OF_INCOME_CONSIDERED_FROM_MINIMUM_WAGE
        scenario[constants.ANNUAL_TAKE_HOME_PAY] = take_home_pay
        plot = [take_home_pay] * 200
        return {
            constants.TYPE: constants.POINTS,
            constants.DATA: plot
        }

    def set_up(self, scenario):
        self.state = scenario.get(constants.STATE)
        self.calendar_year = int(scenario.get(constants.CALENDAR_YEAR))
        self.hours_worked = int(scenario.get(constants.HOURS_WORKED))
        self.min_wage = fetch_min_wage(self.state, self.calendar_year)


class CostOfAttendance(BasePlot):
    def compute(self, scenario):
        academic_year = scenario.get(constants.CALENDAR_YEAR)
        state = scenario.get(constants.STATE)
        living_status = scenario.get(constants.LIVING_STATUS)
        institution_type = scenario.get(constants.INSTITUTION_TYPE)
        tuition_cost_adjustment = float(scenario.get(constants.TUITION_ADJUSTMENT))

        coa = compute_cost_of_attendance(
            year=academic_year,
            state=state,
            living_status=living_status,
            institution_type=institution_type,
            tuition_cost_adjustment=tuition_cost_adjustment
        )

        scenario[constants.COA] = round(coa['tuition'] + coa['non_tuition'])
        scenario[constants.TUITION] = round(coa['tuition'])
        return coa


class StateAppropriation(BasePlot):
    def __init__(self):
        super(StateAppropriation, self).__init__()
        self.institution_type = None
        self.state = None
        self.calendar_year = None
        self.living_status = None
        self.time_to_graduate = None
        self.tuition_adjustment = None
        self.unadjusted_coa = None
        self.adjusted_coa = None

    def set_up(self, scenario):
        self.institution_type = scenario.get(constants.INSTITUTION_TYPE)
        self.state = scenario.get(constants.STATE)
        self.calendar_year = scenario.get(constants.CALENDAR_YEAR)
        self.living_status = scenario.get(constants.LIVING_STATUS)
        self.time_to_graduate = compute_time_to_graduate(scenario)
        self.tuition_adjustment = float(scenario.get(constants.TUITION_ADJUSTMENT))
        self.unadjusted_coa = compute_cost_of_attendance(year=self.calendar_year,
                                                         institution_type=self.institution_type,
                                                         state=self.state,
                                                         living_status=self.living_status)
        self.adjusted_coa = compute_cost_of_attendance(year=self.calendar_year,
                                                       institution_type=self.institution_type,
                                                       state=self.state,
                                                       living_status=self.living_status,
                                                       tuition_cost_adjustment=self.tuition_adjustment)

    def adjust_state_appropriation_with_tuition(self, appropriation_per_student):
        constant = self.unadjusted_coa[constants.TUITION] + appropriation_per_student
        return constant - self.adjusted_coa[constants.TUITION]

    def compute(self, scenario):
        self.set_up(scenario)
        institution_objects = InstitutionModel.objects.filter(institution_type=self.institution_type,
                                                              state=self.state)
        institutions = [institution.institution for institution in institution_objects]

        appropriations = StateAppropriationModel.objects.filter(
            fiscal_year=self.calendar_year,
            institution__in=institutions)

        enrollment = EnrollmentModel.objects.filter(
            academic_year=self.calendar_year,
            institution__in=institutions)

        total_appropriation = 0

        for appr in appropriations:
            total_appropriation += appr.appropriation

        total_appropriation *= 1000
        total_enrollment = 0

        for ennr in enrollment:
            total_enrollment += ennr.fte_enrollment
        if total_enrollment > 0:
            appropriation_per_student = math.floor(total_appropriation / total_enrollment)
        else:
            appropriation_per_student = 0

        appropriation_per_student = self.adjust_state_appropriation_with_tuition(appropriation_per_student)
        plot_data = [appropriation_per_student] * 200
        scenario[constants.TOTAL_APPROPRIATION] = total_appropriation
        scenario[constants.TOTAL_ENROLLMENT] = total_enrollment
        scenario[constants.STATE_APPROPRIATION] = appropriation_per_student
        return {
            constants.TYPE: constants.POINTS,
            constants.DATA: plot_data
        }


class InstitutionalAid(BasePlot):
    # Percent of MFI until SNG is distributed
    SNG_INFLUENCE_MAX_MFI_PERCENT = 70

    USE_WEIGHTED_AVG = 100
    USE_CAMPUS_AID_N = 200
    USE_CAMPUS_AID_Y = 300

    def __init__(self):
        self.living_status = None
        self.institution_type = None

    def set_up(self, scenario):
        self.institution_type = scenario.get(constants.INSTITUTION_TYPE)
        living_status = scenario.get(constants.LIVING_STATUS)
        if living_status in constants.LIVING_STATUS_DEPENDENT:
            self.living_status = constants.DEPENDENT
        elif living_status in constants.LIVING_STATUS_INDEPENDENT:
            self.living_status = constants.INDEPENDENT

        self.state = scenario.get(constants.STATE)
        self.calendar_year = scenario.get(constants.CALENDAR_YEAR)

        self.possible_grants = list(GrantsScholarshipsModel.objects.filter(
            academic_year=self.calendar_year,
            state=self.state,
            institution_type=self.institution_type,
            dependency_status=self.living_status))

    @staticmethod
    def weighted_average(grants):
        weighted_total = 0.0
        total_count = 0.0
        for grant in grants:
            HCY = grant.campus_aid_head_count_sng_y
            CAY = grant.campus_aid_sng_y

            HCN = grant.campus_aid_head_count_sng_n
            CAN = grant.campus_aid_sng_n

            weighted_total += (HCY * CAY) + (HCN * CAN)
            total_count += (HCY + HCN)

        if total_count > 0:
            weighted_average = math.floor(weighted_total / total_count)
        else:
            weighted_average = 0
        return weighted_average

    @staticmethod
    def avg(attribute, iterable):
        return float(sum([getattr(g, attribute) for g in iterable]) / len(iterable))

    @staticmethod
    def decide_averaging_path(percent_mfi, sng_max_influence, always_use_weighted_avg, sng_shown):
        if always_use_weighted_avg:
            return InstitutionalAid.USE_WEIGHTED_AVG
        if sng_shown:
            if percent_mfi <= sng_max_influence:
                return InstitutionalAid.USE_CAMPUS_AID_Y
            else:
                return InstitutionalAid.USE_CAMPUS_AID_N
        else:
            return InstitutionalAid.USE_CAMPUS_AID_N

    def compute(self, scenario):
        self.set_up(scenario)
        plot_data = []
        sng_shown = scenario.get(constants.SNG_SHOWN, True)
        always_use_weighted_avg = constance.config.INSTITUTIONAL_AID_ALWAYS_USE_WEIGHTED_AVG
        for percent_mfi in xrange(1, 201):
            f_percent_mfi = float(percent_mfi) / 100
            grants = filter(lambda m: m.mfi_band_low < f_percent_mfi <= m.mfi_band_high, self.possible_grants)
            averaging_path = self.decide_averaging_path(percent_mfi, self.SNG_INFLUENCE_MAX_MFI_PERCENT,
                                                        always_use_weighted_avg, sng_shown)
            data_point = 0
            if len(grants) <= 0:
                pass

            elif averaging_path == InstitutionalAid.USE_WEIGHTED_AVG:
                data_point = self.weighted_average(grants)

            elif averaging_path == InstitutionalAid.USE_CAMPUS_AID_Y:
                data_point = self.avg(constants.SNG_CAMPUS_AID_Y, grants)

            elif averaging_path == InstitutionalAid.USE_CAMPUS_AID_N:
                data_point = self.avg(constants.SNG_CAMPUS_AID_N, grants)

            plot_data.append(math.floor(data_point))

        return {
            constants.TYPE: constants.POINTS,
            constants.DATA: plot_data
        }


class AffordableDebtPlot(BasePlot):
    def __init__(self):
        self.attainment_attribute = constants.ASSOCIATE_DEGREE
        self.state = None
        self.calendar_year = None
        self.min_wage = None
        self.attainment = None
        self.earnings_exclusion_value = None
        self.earner_percentile = None
        self.R = None
        self.I = None
        self.N = None
        self.affordable_debt_model_data = None
        self.cumulative = None

        self.index_a1_earner = None
        self.data_a1_earner = None
        self.list_of_earners = None
        self.earnings = None

    @staticmethod
    def fetch_data(year, state):
        return [o for o in AffordableDebtModel.objects.filter(calendar_year=year,
                                                              state=state).order_by(constants.PERSON_INCOME_LOWER_BOUND)
                ]

    @staticmethod
    def percentile_of_exluded_earner(year, state, exclusion_level, attainment_attribute):
        if not constance.config.SHOW_PERCENTILE_OF_EXCLUDED_EARNER:
            return None
        cache_key = util.generate_cache_key('percentile_of_excluded_earner', year=year, state=state,
                                            exclusion_level=exclusion_level, attainment_attribute=attainment_attribute)
        result = cache.get(cache_key)
        if not result:
            affordable_debt_models = AffordableDebtPlot.fetch_data(year, state)
            debt_models = filter(lambda d: d.person_income_lower_bound != 0, affordable_debt_models)
            percentiles = AffordableDebtPlot.compute_percentiles(debt_models, attainment_attribute)
            result = interp1d(x=[d.person_income_lower_bound for d in debt_models], y=percentiles)(exclusion_level)
            cache.set(cache_key, result)
        return float(result)

    @staticmethod
    def compute_percentiles(affordable_debt_models, attainment_attribute):
        percentiles = []
        total = sum((getattr(adm, attainment_attribute) for adm in affordable_debt_models))
        cumulative = 0.0
        for adm in affordable_debt_models:
            cumulative += getattr(adm, attainment_attribute)
            percentiles.append(round(cumulative * 100 / total))
        return percentiles

    @staticmethod
    def get_interpolation_data(year, state, earnings_exclusion_value, attainment_attribute):
        cache_key = util.generate_cache_key(function_name='affordable_debt_model_interpolate',
                                            year=year,
                                            state=state,
                                            earnings_exclusion_value=earnings_exclusion_value,
                                            attainment_attribute=attainment_attribute)
        interpolated_earnings = cache.get(cache_key)
        if not interpolated_earnings:
            affordable_debt_model_data = AffordableDebtPlot.fetch_data(year, state)
            list_of_earners = filter(lambda d: d.person_income_lower_bound > earnings_exclusion_value,
                                     affordable_debt_model_data)
            percentiles = AffordableDebtPlot.compute_percentiles(list_of_earners, attainment_attribute)
            earnings_from_db = [adm.person_income_upper_bound for adm in list_of_earners]
            interpolator = interp1d(x=percentiles, y=earnings_from_db, bounds_error=False, fill_value=None)
            interpolated_earnings = {percentile: interpolator(percentile) for percentile in range(1, 101)}
            cache.set(cache_key, interpolated_earnings, settings.CACHE_LENGTH)
        return interpolated_earnings

    @staticmethod
    def interpolate(year, state, earnings_exclusion_value, earner_percentile, max_earnings, attainment_attribute):
        interpolated_earnings = AffordableDebtPlot.get_interpolation_data(year, state, earnings_exclusion_value,
                                                                          attainment_attribute)
        actual_percentile = earner_percentile
        actual_earnings = interpolated_earnings[actual_percentile]
        while actual_earnings > max_earnings and actual_percentile >= 1:
            actual_percentile -= 1
            actual_earnings = interpolated_earnings[actual_percentile]

        return actual_percentile, actual_earnings

    def set_up(self, scenario):
        self.attainment = compute_time_to_graduate(scenario)

        # Needed for filtering data
        self.state = scenario.get(constants.STATE)
        self.calendar_year = int(scenario.get(constants.CALENDAR_YEAR))
        self.earnings_exclusion_value = constance.config.DEFAULT_ANNUAL_EARNING_EXCLUSION_LEVEL
        self.attainment_attribute = constants.BACHELORS_DEGREE if self.attainment >= 4 else constants.ASSOCIATE_DEGREE

        # Needed to compute debt
        self.earner_percentile = int(scenario.get(constants.EARNINGS_PERCENTILE))
        self.R = float(scenario.get(constants.LOAN_REPAYMENT_RATIO, 1)) / 100
        self.I = float(scenario.get(constants.INTEREST_ON_DEBT)) / 100
        self.N = float(scenario.get(constants.LOAN_DURATION))

        self.earner_percentile, self.earnings = self.interpolate(self.calendar_year, self.state,
                                                                 self.earnings_exclusion_value,
                                                                 self.earner_percentile,
                                                                 constance.config.MAX_ALLOWED_EARNINGS,
                                                                 self.attainment_attribute)

        scenario[constants.EARNINGS_PERCENTILE] = self.earner_percentile
        scenario[constants.PERCENTILE_OF_EXCLUDED_EARNER] = self.percentile_of_exluded_earner(
            self.calendar_year, self.state,
            self.earnings_exclusion_value,
            self.attainment_attribute)

    def __hash__(self):
        return super(AffordableDebtPlot, self).__hash__()

    def compute(self, scenario):
        try:
            self.set_up(scenario)
            a1_dollar_value = float(self.earnings)
        except Exception as e:
            logging.exception("Couldn't compute Affordable Debt")
            return {
                constants.TYPE: constants.POINTS,
                constants.DATA: [0] * 200,
                constants.ERROR: str(e)
            }

        scenario[constants.EARNINGS_ANNUAL] = a1_dollar_value
        max_monthly_payment = a1_dollar_value * self.R / 12
        number_of_payments = self.N * 12

        if self.I > 0:
            monthly_interest_rate = self.I / 12
            step1 = max_monthly_payment * (math.pow(1 + monthly_interest_rate, number_of_payments) - 1)
            step2 = monthly_interest_rate * math.pow(1 + monthly_interest_rate, number_of_payments)
            debt_max = step1 / step2
        else:
            debt_max = max_monthly_payment * number_of_payments

        return {
            constants.TYPE: constants.POINTS,
            constants.DATA: [math.floor(debt_max / self.attainment)] * 200
        }
