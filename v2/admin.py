from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from v2.admin_resources import *


# Register your models here.
@admin.register(PovertyGuidelineModel)
class PovertyGuidelineModelAdmin(ImportExportModelAdmin):
    list_display = PovertyGuidelineModel._meta.get_all_field_names()
    resource_class = PovertyGuidelineModelResource


@admin.register(MedianFamilyIncomeModel)
class MedianFamilyIncomeModelAdmin(ImportExportModelAdmin):
    list_display = MedianFamilyIncomeModel._meta.get_all_field_names()
    resource_class = MedianFamilyIncomeModelResource


@admin.register(PellGrantModel)
class PellGrantModelAdmin(ImportExportModelAdmin):
    list_display = PellGrantModel._meta.get_all_field_names()
    resource_class = PellGrantModelResource
    list_filter = ('academic_year', 'efc_lower', 'efc_upper', 'coa_lower', 'coa_upper')


@admin.register(ExpectedFamilyContributionModel)
class ExpectedFamilyContributionModelAdmin(ImportExportModelAdmin):
    list_display = ExpectedFamilyContributionModel._meta.get_all_field_names()
    resource_class = ExpectedFamilyContributionModelResource


@admin.register(StateNeedGrantDistributionScheduleModel)
class StateNeedGrantDistributionScheduleModelAdmin(ImportExportModelAdmin):
    list_display = StateNeedGrantDistributionScheduleModel._meta.get_all_field_names()
    resource_class = StateNeedGrantDistributionScheduleModelResource


@admin.register(StateNeedGrantMaxAwardModel)
class StateNeedGrantMaxAwardModelAdmin(ImportExportModelAdmin):
    list_display = StateNeedGrantMaxAwardModel._meta.get_all_field_names()
    resource_class = StateNeedGrantMaxAwardModelResource


@admin.register(MinimumWageModel)
class MinimumWageModelAdmin(ImportExportModelAdmin):
    list_display = MinimumWageModel._meta.get_all_field_names()
    resource_class = MinimumWageModelResource


@admin.register(NonTuitionCostsModel)
class NonTuitionCostsModelAdmin(ImportExportModelAdmin):
    list_display = NonTuitionCostsModel._meta.get_all_field_names()
    resource_class = NonTuitionCostsModelResource


@admin.register(TuitionCostsModel)
class TuitionCostsModelAdmin(ImportExportModelAdmin):
    list_display = TuitionCostsModel._meta.get_all_field_names()
    resource_class = TuitionCostsModelResource


@admin.register(InstitutionModel)
class InstitutionModelAdmin(ImportExportModelAdmin):
    list_display = InstitutionModel._meta.get_all_field_names()
    resource_class = InstitutionModelResource


@admin.register(EnrollmentModel)
class EnrollmentModelAdmin(ImportExportModelAdmin):
    list_display = EnrollmentModel._meta.get_all_field_names()
    resource_class = EnrollmentModelResource


@admin.register(StateAppropriationModel)
class StateAppropriationModelAdmin(ImportExportModelAdmin):
    list_display = StateAppropriationModel._meta.get_all_field_names()
    resource_class = StateAppropriationModelResource


@admin.register(GrantsScholarshipsModel)
class GrantsScholarshipsModelAdmin(ImportExportModelAdmin):
    list_display = ['id',
                    'academic_year',
                    'state',
                    'institution_type',
                    'dependency_status',

                    'mfi_band_low',
                    'mfi_band_high',
                    'head_count',

                    'federal_head_count',
                    'federal_grants',

                    'state_head_count',
                    'state_grants',

                    'work_study_head_count',
                    'work_study_earnings',

                    'campus_aid_head_count_sng_y',
                    'campus_aid_sng_y',
                    'campus_aid_head_count_sng_n',
                    'campus_aid_sng_n',

                    'loan_head_count',
                    'loans',
                    'loan_no_plus_head_count',
                    'loans_no_plus']
    resource_class = GrantsScholarshipsModelResource


@admin.register(AffordableDebtModel)
class AffordableDebtModelAdmin(ImportExportModelAdmin):
    list_display = AffordableDebtModel._meta.get_all_field_names()
    list_filter = ('calendar_year', 'state', 'person_income_lower_bound')
    resource_class = AffordableDebtModelResource
