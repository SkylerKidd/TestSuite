from proto1.scenario import KEY_DISCRETIONARY_INCOME
from proto1.transform.base import BaseTransform


class DiscretionaryIncomeTransform(BaseTransform):
    def __init__(self, list_percent_median_incomes, median_family_income, poverty_guideline):
        super(DiscretionaryIncomeTransform, self).__init__()
        self.poverty_guideline = poverty_guideline
        self.median_family_income = median_family_income
        self.list_percent_median_incomes = list_percent_median_incomes

    def transform(self, scenario):
        if not scenario.has_key(KEY_DISCRETIONARY_INCOME):
            scenario[KEY_DISCRETIONARY_INCOME] = {}

        scenario[KEY_DISCRETIONARY_INCOME][
            (self.poverty_guideline, self.median_family_income)] = discretionary_incomes = []

        for percent_median_income in self.list_percent_median_incomes:
            family_income = percent_median_income * self.median_family_income.income / 100
            poverty_guideline_for_family_of_4 = self.poverty_guideline.first_person + 3 * self.poverty_guideline.each_additional_person
            disc_income = family_income - poverty_guideline_for_family_of_4
            discretionary_incomes.append(disc_income)
        return scenario
