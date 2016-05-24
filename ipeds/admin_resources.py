from import_export import resources

from ipeds.models import *


class InstitutionModelResource(resources.ModelResource):
    class Meta:
        model = InstitutionModel


class EnrollmentModelResource(resources.ModelResource):
    class Meta:
        model = EnrollmentModel


class AppropriationModelResource(resources.ModelResource):
    class Meta:
        model = AppropriationsModel


class TuitionModelResource(resources.ModelResource):
    class Meta:
        model = TuitionModel


class NonTuitionModelResource(resources.ModelResource):
    class Meta:
        model = NonTuitionModel
