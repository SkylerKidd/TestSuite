import math

import ipeds.plots
from v2 import constants
from v2.plots import washington
from v2.plots.base_plot import BasePlot
from v2.transform import compute_median_family_income

MAX_EFC = 5088


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

    def pre_compute(self):
        super(StateNeedGrantPlot, self).pre_compute()
        self.institution_type = self.scenario.get(constants.INSTITUTION_TYPE)

    def compute(self):
        plot_data = []
        for percent_of_median_income in xrange(1, 201):
            income = float(self.median_family_income) * percent_of_median_income / 100
            efc = self.compute_expected_family_contribution(income)
            if self.institution_type in ['Public Research', 'Public Regional']:
                if efc < MAX_EFC:
                    plot_data.append(5000)
                else:
                    plot_data.append(0)
            elif self.institution_type == 'CTCS':
                plot_data.append(1350)
            elif self.institution_type == 'Private Nonprofit':
                if efc < 1000:
                    plot_data.append(5046)
                else:
                    plot_data.append(3364)
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
