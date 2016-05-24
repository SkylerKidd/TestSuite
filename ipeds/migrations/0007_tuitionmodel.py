# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipeds', '0006_auto_20160318_0124'),
    ]

    operations = [
        migrations.CreateModel(
            name='TuitionModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('academic_year', models.IntegerField(db_index=True)),
                ('institution_id', models.IntegerField(db_index=True)),
                ('in_district_avg_tuition_full_time_undergraduate', models.IntegerField(default=None, null=True, blank=True)),
                ('in_district_fee_full_time_undergraduate', models.IntegerField(default=None, null=True, blank=True)),
                ('in_state_avg_tuition_full_time_undergraduate', models.IntegerField(default=None, null=True, blank=True)),
                ('in_state_fee_full_time_undergraduate', models.IntegerField(default=None, null=True, blank=True)),
                ('published_in_district_tuition', models.IntegerField(default=None, null=True, blank=True)),
                ('published_in_district_fees', models.IntegerField(default=None, null=True, blank=True)),
                ('published_in_district_tuition_and_fees', models.IntegerField(default=None, null=True, blank=True)),
                ('published_in_state_tuition', models.IntegerField(default=None, null=True, blank=True)),
                ('published_in_state_fees', models.IntegerField(default=None, null=True, blank=True)),
                ('published_in_state_tuition_and_fees', models.IntegerField(default=None, null=True, blank=True)),
            ],
        ),
    ]
