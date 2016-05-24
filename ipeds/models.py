from django.db import models


# Create your models here.

class InstitutionModel(models.Model):
    institution_id = models.IntegerField(default=None, blank=True, null=True)
    institution = models.CharField(max_length=255)
    state_abbreviation = models.CharField(max_length=50, blank=True, null=True)
    institution_type = models.IntegerField(default=None, db_index=True, blank=True, null=True)
    institution_type_and_level = models.IntegerField(default=None, db_index=True, blank=True, null=True)
    institution_level = models.IntegerField(default=None, db_index=True, blank=True, null=True)
    carnegie_classification = models.IntegerField(default=None, db_index=True, blank=True, null=True)
    land_grant_institution = models.IntegerField(default=None, db_index=True, blank=True, null=True)
    historically_black_colleges_and_universities = models.IntegerField(default=None, db_index=True, blank=True,
                                                                       null=True)
    tribal = models.IntegerField(default=None, db_index=True, blank=True, null=True)
    institutional_control_or_affiliation = models.IntegerField(default=None, db_index=True, blank=True, null=True)
    academic_year = models.IntegerField(db_index=True, blank=True, null=True)

    class Meta:
        unique_together = ('institution_id', 'academic_year')


class EnrollmentModel(models.Model):
    institution_id = models.IntegerField(db_index=True)
    estimated_fte_undergraduate = models.IntegerField(default=None, blank=True, null=True)
    reported_fte_undergraduate = models.IntegerField(default=None, blank=True, null=True)
    academic_year = models.IntegerField(db_index=True)

    class Meta:
        unique_together = ('institution_id', 'academic_year')


class AppropriationsModel(models.Model):
    institution_id = models.IntegerField(db_index=True)
    fiscal_year = models.IntegerField(db_index=True)
    state_appropriation = models.IntegerField(db_index=True)
    local_appropriation = models.IntegerField(db_index=True)

    class Meta:
        unique_together = ('institution_id', 'fiscal_year')


class TuitionModel(models.Model):
    academic_year = models.IntegerField(db_index=True)
    institution_id = models.IntegerField(db_index=True)
    in_district_avg_tuition_full_time_undergraduate = models.IntegerField(default=None, blank=True, null=True)
    in_district_fee_full_time_undergraduate = models.IntegerField(default=None, blank=True, null=True)
    in_state_avg_tuition_full_time_undergraduate = models.IntegerField(default=None, blank=True, null=True)
    in_state_fee_full_time_undergraduate = models.IntegerField(default=None, blank=True, null=True)
    published_in_district_tuition = models.IntegerField(default=None, blank=True, null=True)
    published_in_district_fees = models.IntegerField(default=None, blank=True, null=True)
    published_in_district_tuition_and_fees = models.IntegerField(default=None, blank=True, null=True)
    published_in_state_tuition = models.IntegerField(default=None, blank=True, null=True)
    published_in_state_fees = models.IntegerField(default=None, blank=True, null=True)
    published_in_state_tuition_and_fees = models.IntegerField(default=None, blank=True, null=True)

    class Meta:
        unique_together = ('institution_id', 'academic_year')


class NonTuitionModel(models.Model):
    academic_year = models.IntegerField(db_index=True)
    institution_id = models.IntegerField(db_index=True)
    books = models.IntegerField(default=None, blank=True, null=True)
    room_and_board_on_campus = models.IntegerField(default=None, blank=True, null=True)
    transportation_and_misc_on_campus = models.IntegerField(default=None, blank=True, null=True)
    room_and_board_off_campus_not_with_family = models.IntegerField(default=None, blank=True, null=True)
    transportation_and_misc_off_campus_not_with_family = models.IntegerField(default=None, blank=True, null=True)
    transportation_and_misc_off_campus_with_family = models.IntegerField(default=None, blank=True, null=True)

    class Meta:
        unique_together = ('institution_id', 'academic_year')

    def total_on_campus(self):
        return self.books + self.room_and_board_on_campus + self.transportation_and_misc_on_campus

    def total_off_campus(self):
        return self.books + self.room_and_board_off_campus_not_with_family + self.transportation_and_misc_off_campus_not_with_family

    def total_off_campus_with_family(self):
        return self.books + (
            self.room_and_board_off_campus_not_with_family * 0.33) + self.transportation_and_misc_off_campus_not_with_family
