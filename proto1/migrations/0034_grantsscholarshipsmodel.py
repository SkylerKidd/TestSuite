# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto1', '0033_auto_20151227_2350'),
    ]

    operations = [
        migrations.CreateModel(
            name='GrantsScholarshipsModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('academic_year', models.IntegerField()),
                ('state', models.CharField(max_length=50)),
                ('institution_type', models.CharField(max_length=50)),
                ('dependency_status', models.CharField(max_length=100)),
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
    ]
