# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto1', '0036_povertyguidelinemodel_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='AffordableDebtModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('calendar_year', models.IntegerField(db_index=True)),
                ('state', models.CharField(max_length=50, db_index=True)),
                ('person_income_lower_bound', models.IntegerField()),
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
    ]
