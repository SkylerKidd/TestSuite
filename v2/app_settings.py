REGISTERED_PLOTS = {
    'family_income': 'v2.plots.washington.FamilyIncomePlot',
    'college_savings': 'v2.plots.washington.CollegeSavingsPlot',
    'state_need_grant': 'v2.plots.washington.StateNeedGrantPlot',
    'pell_grant': 'v2.plots.washington.PellGrantPlot',
    'student_work': 'v2.plots.washington.MinimumWagePlot',
    'cost_of_attendance': 'v2.plots.washington.CostOfAttendance',
    'state_appropriation': 'v2.plots.washington.StateAppropriation',
    'institutional_aid': 'v2.plots.washington.InstitutionalAid',
    'affordable_debt': 'v2.plots.washington.AffordableDebtPlot'

}

ALLOWED_STATES = [
    'washington',
    'mississippi',
    'texas'
]


class PlotClassMapping(object):
    PACKAGE = 'v2.plots'
    MODULES = {state: '.' + state for state in ALLOWED_STATES}
    DEFAULT_MODULE = MODULES[ALLOWED_STATES[0]]
    PLOTS = {
        'family_income': 'FamilyIncomePlot',
        'college_savings': 'CollegeSavingsPlot',
        'state_need_grant': 'StateNeedGrantPlot',
        'pell_grant': 'PellGrantPlot',
        'student_work': 'MinimumWagePlot',
        'cost_of_attendance': 'CostOfAttendance',
        'state_appropriation': 'StateAppropriation',
        'institutional_aid': 'InstitutionalAid',
        'affordable_debt': 'AffordableDebtPlot'

    }
