import math

import ipeds.plots
from ipeds.query_helpers import compute_cost_of_attendance
from v2 import constants
from v2.plots import washington
from v2.plots.base_plot import BasePlot
from v2.plots.common_utils import compute_time_to_graduate
from v2.transform import compute_median_family_income


class FamilyIncomePlot(washington.FamilyIncomePlot):
    pass


class CollegeSavingsPlot(washington.CollegeSavingsPlot):
    pass


class StateNeedGrantPlot(ipeds.plots.StateNeedGrantPlot):
    def compute_expected_family_contribution(self, income):
        efc = math.floor(0.31 * income - 14420.03)
        return efc if efc > 0 else 0

    def query_db(self):
        super(StateNeedGrantPlot, self).query_db()
        self.median_family_income = compute_median_family_income(self.scenario)
        self.time_to_graduate = compute_time_to_graduate(self.scenario)
        self.expected_state_aid = 3000 / self.time_to_graduate

    def pre_compute(self):
        super(StateNeedGrantPlot, self).pre_compute()
        academic_year = self.scenario.get(constants.CALENDAR_YEAR)
        state = self.scenario.get(constants.STATE)
        living_status = self.scenario.get(constants.LIVING_STATUS)
        institution_type = self.scenario.get(constants.INSTITUTION_TYPE)
        tuition_cost_adjustment = float(self.scenario.get(constants.TUITION_ADJUSTMENT))

        self.coa = compute_cost_of_attendance(
            year=academic_year,
            state=state,
            living_status=living_status,
            institution_type=institution_type,
            tuition_cost_adjustment=tuition_cost_adjustment
        )

    def award_adjustment(self, award):
        state_financial_aid_adjustment = int(self.scenario.get('state_financial_aid_adjustment', 100))
        return award * state_financial_aid_adjustment / 100

    def compute(self):
        plot_data = []
        for percent_of_median_income in xrange(1, 201):
            income = float(self.median_family_income) * percent_of_median_income / 100
            efc = self.compute_expected_family_contribution(income)
            if efc > 0:
                current_award = self.expected_state_aid
            else:
                current_award = 0
            if income < 39500 + 5000:
                help_grant = self.coa[constants.TUITION]
                current_award += self.award_adjustment(help_grant)
            plot_data.append(current_award)
        return {
            constants.TYPE: constants.POINTS,
            constants.DATA: plot_data
        }


class PellGrantPlot(washington.PellGrantPlot):
    pass


class MinimumWagePlot(washington.MinimumWagePlot):
    pass


class AffordableDebtPlot(washington.AffordableDebtPlot):
    pass


class StateAppropriation(ipeds.plots.StateAppropriation):
    pass


class InstitutionalAid(BasePlot):
    def compute(self):
        super(InstitutionalAid, self).compute()
        return {
            constants.TYPE: constants.POINTS,
            constants.DATA: [0] * 200
        }


class CostOfAttendance(ipeds.plots.CostOfAttendance):
    pass
