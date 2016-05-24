from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin

from ipeds.admin_resources import *
from ipeds.models import *


@admin.register(InstitutionModel)
class InstitutionModelAdmin(ImportExportModelAdmin):
    resource_class = InstitutionModelResource
    list_display = InstitutionModel._meta.get_all_field_names()
    list_filter = ('academic_year', 'state_abbreviation', 'institution_id')


@admin.register(EnrollmentModel)
class EnrollmentModelAdmin(ImportExportModelAdmin):
    resource_class = EnrollmentModelResource
    list_display = EnrollmentModel._meta.get_all_field_names()
    list_filter = ('academic_year', 'institution_id')


@admin.register(AppropriationsModel)
class AppropriationsModelAdmin(ImportExportModelAdmin):
    resource_class = AppropriationModelResource
    list_display = AppropriationsModel._meta.get_all_field_names()
    list_filter = ('fiscal_year', 'institution_id')


@admin.register(TuitionModel)
class TuitionModelAdmin(ImportExportModelAdmin):
    resource_class = TuitionModelResource
    list_display = TuitionModel._meta.get_all_field_names()
    list_filter = ('academic_year', 'institution_id')


@admin.register(NonTuitionModel)
class NonTuitionModelAdmin(ImportExportModelAdmin):
    resource_class = NonTuitionModelResource
    list_display = NonTuitionModel._meta.get_all_field_names()
    list_filter = ('academic_year', 'institution_id')

