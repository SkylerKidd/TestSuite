# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AffordableDebtModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('calendar_year', models.IntegerField(db_index=True)),
                ('state', models.CharField(max_length=50, db_index=True)),
                ('person_income_lower_bound', models.IntegerField()),
                ('person_income_upper_bound', models.IntegerField()),
                ('totals', models.IntegerField()),
                ('less_than_9th_grade', models.IntegerField()),
                ('no_diploma_9th_12th_grade', models.IntegerField()),
                ('high_school_diploma_or_equivalent', models.IntegerField()),
                ('some_college_no_assoc_or_4_yr_degree', models.IntegerField()),
                ('associate_degree', models.IntegerField()),
                ('bachelors_degree', models.IntegerField()),
                ('masters_degree', models.IntegerField()),
                ('professional_degree', models.IntegerField()),
                ('doctorate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EnrollmentModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.CharField(max_length=50, db_index=True)),
                ('institution', models.CharField(max_length=100)),
                ('academic_year', models.IntegerField(db_index=True)),
                ('fte_enrollment', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ExpectedFamilyContributionModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('family_income', models.IntegerField()),
                ('expected_family_contribution', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='GrantsScholarshipsModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('academic_year', models.IntegerField(db_index=True)),
                ('state', models.CharField(max_length=50, db_index=True)),
                ('institution_type', models.CharField(max_length=50, db_index=True)),
                ('dependency_status', models.CharField(max_length=100, db_index=True)),
                ('mfi_band_low', models.FloatField()),
                ('mfi_band_high', models.FloatField()),
                ('head_count', models.IntegerField()),
                ('federal_head_count', models.IntegerField()),
                ('federal_grants', models.IntegerField()),
                ('state_head_count', models.IntegerField()),
                ('state_grants', models.IntegerField()),
                ('work_study_head_count', models.IntegerField()),
                ('work_study_earnings', models.FloatField()),
                ('campus_aid_head_count_sng_y', models.IntegerField()),
                ('campus_aid_sng_y', models.FloatField()),
                ('campus_aid_head_count_sng_n', models.IntegerField()),
                ('campus_aid_sng_n', models.FloatField()),
                ('loan_head_count', models.IntegerField()),
                ('loans', models.FloatField()),
                ('loan_no_plus_head_count', models.IntegerField()),
                ('loans_no_plus', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='InstitutionModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.CharField(max_length=50, db_index=True)),
                ('institution', models.CharField(max_length=100)),
                ('institution_type', models.CharField(max_length=50, db_index=True)),
                ('nominal_time_to_graduate', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='MedianFamilyIncomeModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.CharField(max_length=50, db_index=True)),
                ('year', models.IntegerField(db_index=True)),
                ('income', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MinimumWageModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('calendar_year', models.IntegerField(db_index=True)),
                ('state', models.CharField(max_length=50, db_index=True)),
                ('minimum_wage', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='NonTuitionCostsModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('academic_year', models.IntegerField(db_index=True)),
                ('state', models.CharField(max_length=50, db_index=True)),
                ('living_status', models.CharField(max_length=100, db_index=True)),
                ('books', models.FloatField()),
                ('room_and_board', models.FloatField()),
                ('transportation', models.FloatField()),
                ('miscellaneous', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PellGrantModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coa_lower', models.IntegerField()),
                ('coa_upper', models.IntegerField()),
                ('efc_lower', models.IntegerField()),
                ('efc_upper', models.IntegerField()),
                ('academic_year', models.IntegerField(db_index=True)),
                ('pell_award', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PovertyGuidelineModel',
            fields=[
                ('id', models.AutoField(default=None, serialize=False, primary_key=True)),
                ('year', models.IntegerField(db_index=True)),
                ('first_person', models.IntegerField()),
                ('each_additional_person', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StateAppropriationModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.CharField(max_length=50)),
                ('fiscal_year', models.IntegerField(db_index=True)),
                ('institution', models.CharField(max_length=100)),
                ('appropriation', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='StateNeedGrantDistributionScheduleModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('academic_year', models.IntegerField(db_index=True)),
                ('percent_mfi_lower', models.IntegerField()),
                ('percent_mfi_upper', models.IntegerField()),
                ('percent_of_max_award', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='StateNeedGrantMaxAwardModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('academic_year', models.IntegerField(db_index=True)),
                ('institution_type', models.CharField(max_length=50, db_index=True)),
                ('sng_max_award', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='TuitionCostsModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('academic_year', models.IntegerField(db_index=True)),
                ('state', models.CharField(max_length=50, db_index=True)),
                ('institution', models.CharField(max_length=100, db_index=True)),
                ('tuition_and_fees', models.FloatField()),
            ],
        ),
    ]
