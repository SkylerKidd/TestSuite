from import_export import resources

from v2.models import *


class PovertyGuidelineModelResource(resources.ModelResource):
    class Meta:
        model = PovertyGuidelineModel


class MedianFamilyIncomeModelResource(resources.ModelResource):
    class Meta:
        model = MedianFamilyIncomeModel


class PellGrantModelResource(resources.ModelResource):
    class Meta:
        model = PellGrantModel


class ExpectedFamilyContributionModelResource(resources.ModelResource):
    class Meta:
        model = ExpectedFamilyContributionModel


class StateNeedGrantDistributionScheduleModelResource(resources.ModelResource):
    class Meta:
        model = StateNeedGrantDistributionScheduleModel


class StateNeedGrantMaxAwardModelResource(resources.ModelResource):
    class Meta:
        model = StateNeedGrantMaxAwardModel


class MinimumWageModelResource(resources.ModelResource):
    class Meta:
        model = MinimumWageModel


class NonTuitionCostsModelResource(resources.ModelResource):
    class Meta:
        model = NonTuitionCostsModel


class TuitionCostsModelResource(resources.ModelResource):
    class Meta:
        model = TuitionCostsModel


class InstitutionModelResource(resources.ModelResource):
    class Meta:
        model = InstitutionModel


class EnrollmentModelResource(resources.ModelResource):
    class Meta:
        model = EnrollmentModel


class StateAppropriationModelResource(resources.ModelResource):
    class Meta:
        model = StateAppropriationModel


class GrantsScholarshipsModelResource(resources.ModelResource):
    class Meta:
        model = GrantsScholarshipsModel


class AffordableDebtModelResource(resources.ModelResource):
    class Meta:
        model = AffordableDebtModel
