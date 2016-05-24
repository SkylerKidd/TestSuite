from v2 import constants

__author__ = 'gautam'

KEY_POVERTY_GUIDELINE = 'poverty_guideline'
KEY_MEDIAN_FAMILY_INCOME = 'median_family_income'
KEY_DISCRETIONARY_INCOME = 'discretionary_income'
KEY_STATE_NEED_GRANT_MAX_AWARD = 'state_need_grant_max_award'
KEY_STATE_NEED_GRANT_DISTRIBUTION_SCHEDULE = 'state_need_grant_distribution_schedule'
KEY_MINIMUM_WAGE = 'minimum_wage'
KEY_COLLEGE_SAVINGS = 'college_savings'
KEY_TUITION_COST = 'tuition_cost'
KEY_NON_TUITION_COST = 'non_tuition_cost'


class Scenario(dict):
    def __init__(self, *args, **kwargs):
        super(Scenario, self).__init__(*args, **kwargs)

    def get_state(self):
        return self.get(constants.STATE, '').lower()
