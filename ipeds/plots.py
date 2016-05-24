from ipeds.models import EnrollmentModel, AppropriationsModel
from ipeds.query_helpers import compute_cost_of_attendance, query_institutions
from v2 import constants
from v2.plots.base_plot import BasePlot


class CostOfAttendance(BasePlot):
    def compute(self):
        academic_year = self.scenario.get(constants.CALENDAR_YEAR)
        state = self.scenario.get(constants.STATE)
        living_status = self.scenario.get(constants.LIVING_STATUS)
        institution_type = self.scenario.get(constants.INSTITUTION_TYPE)
        tuition_cost_adjustment = float(self.scenario.get(constants.TUITION_ADJUSTMENT))

        coa = compute_cost_of_attendance(
            year=academic_year,
            state=state,
            living_status=living_status,
            institution_type=institution_type,
            tuition_cost_adjustment=tuition_cost_adjustment
        )

        self.scenario[constants.COA] = round(coa['tuition'] + coa['non_tuition'])
        self.scenario[constants.TUITION] = round(coa['tuition'])
        return coa


class StateAppropriation(BasePlot):
    def query_ipeds(self):
        self.institutions = query_institutions(self.institution_type, self.state, self.calendar_year)
        self.institution_ids = [i.institution_id for i in self.institutions]
        self.enrollments = EnrollmentModel.objects.filter(institution_id__in=self.institution_ids,
                                                          reported_fte_undergraduate__isnull=False)

        self.appropriations = AppropriationsModel.objects.filter(
            institution_id__in=[e.institution_id for e in self.enrollments]).order_by('institution_id')

    def query_db(self):
        super(StateAppropriation, self).query_db()
        scenario = self.scenario
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
        self.query_ipeds()

    def pre_compute(self):
        super(StateAppropriation, self).pre_compute()
        self.appropriation_map = {}
        for e in self.enrollments:
            self.appropriation_map[e.institution_id] = {'enrollment': e.estimated_fte_undergraduate}
        for a in self.appropriations:
            self.appropriation_map[a.institution_id]['appropriation'] = a.state_appropriation

    def post_compute(self):
        super(StateAppropriation, self).post_compute()

    def compute(self):
        super(StateAppropriation, self).compute()
        appropriations_per_student = []
        for k, value in self.appropriation_map.iteritems():
            appropriations_per_student.append(value.get('appropriation', 0) / value['enrollment'])
        appropriation_per_student = sum(appropriations_per_student) / len(appropriations_per_student)
        self.scenario['institutions'] = [i.institution for i in self.institutions]
        return {
            constants.TYPE: constants.POINTS,
            constants.DATA: [appropriation_per_student] * 200
        }


class StateNeedGrantPlot(BasePlot):
    def query_db(self):
        super(StateNeedGrantPlot, self).query_db()

    def compute(self):
        super(StateNeedGrantPlot, self).compute()
        return {
            constants.TYPE: constants.POINTS,
            constants.DATA: [0] * 200
        }

    def pre_compute(self):
        super(StateNeedGrantPlot, self).pre_compute()
