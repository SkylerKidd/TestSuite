import math

from v2 import constants
from v2.scenario import KEY_COLLEGE_SAVINGS
from v2.transform.base import BaseTransform

COMPOUNDING_TWICE_PER_YEAR = 2


class CompoundInterestTransform(BaseTransform):
    def __init__(self, plot_data):
        super(CompoundInterestTransform, self).__init__()
        self.plot_data = plot_data

    @staticmethod
    def compound_interest(A, n, i, t):
        F = (A / 12) * (math.pow((1 + i / 12), n * 12) - 1) / (i / 12)
        return F

    def transform(self, scenario):
        scenario[KEY_COLLEGE_SAVINGS] = plot_data = []
        for saving in self.plot_data:
            starting_amount = saving
            years_of_savings = int(scenario.get(constants.YEARS_OF_SAVING))
            interest_earned = float(scenario.get(constants.INTEREST_EARNED))
            plot_data.append(self.compound_interest(
                starting_amount,
                COMPOUNDING_TWICE_PER_YEAR,
                float(interest_earned / 100),
                years_of_savings))
        return plot_data
