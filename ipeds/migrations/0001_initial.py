# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InstitutionModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('institution_id', models.IntegerField(default=None)),
                ('institution', models.CharField(max_length=255)),
                ('state_abbreviation', models.CharField(max_length=50)),
                ('institution_type', models.IntegerField(default=None, db_index=True)),
                ('institution_type_and_level', models.IntegerField(default=None, db_index=True)),
                ('institution_level', models.IntegerField(default=None, db_index=True)),
                ('carnegie_classification', models.IntegerField(default=None, db_index=True)),
                ('land_grant_institution', models.IntegerField(default=None, db_index=True)),
                ('historically_black_colleges_and_universities', models.IntegerField(default=None, db_index=True)),
                ('tribal', models.IntegerField(default=None, db_index=True)),
                ('institutional_control_or_affiliation', models.IntegerField(default=None, db_index=True)),
                ('academic_year', models.IntegerField(db_index=True)),
            ],
        ),
    ]
