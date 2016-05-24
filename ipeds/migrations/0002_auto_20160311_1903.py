# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipeds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institutionmodel',
            name='academic_year',
            field=models.IntegerField(db_index=True, blank=True),
        ),
        migrations.AlterField(
            model_name='institutionmodel',
            name='carnegie_classification',
            field=models.IntegerField(default=None, db_index=True, blank=True),
        ),
        migrations.AlterField(
            model_name='institutionmodel',
            name='historically_black_colleges_and_universities',
            field=models.IntegerField(default=None, db_index=True, blank=True),
        ),
        migrations.AlterField(
            model_name='institutionmodel',
            name='institution_id',
            field=models.IntegerField(default=None, blank=True),
        ),
        migrations.AlterField(
            model_name='institutionmodel',
            name='institution_level',
            field=models.IntegerField(default=None, db_index=True, blank=True),
        ),
        migrations.AlterField(
            model_name='institutionmodel',
            name='institution_type',
            field=models.IntegerField(default=None, db_index=True, blank=True),
        ),
        migrations.AlterField(
            model_name='institutionmodel',
            name='institution_type_and_level',
            field=models.IntegerField(default=None, db_index=True, blank=True),
        ),
        migrations.AlterField(
            model_name='institutionmodel',
            name='institutional_control_or_affiliation',
            field=models.IntegerField(default=None, db_index=True, blank=True),
        ),
        migrations.AlterField(
            model_name='institutionmodel',
            name='land_grant_institution',
            field=models.IntegerField(default=None, db_index=True, blank=True),
        ),
        migrations.AlterField(
            model_name='institutionmodel',
            name='state_abbreviation',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='institutionmodel',
            name='tribal',
            field=models.IntegerField(default=None, db_index=True, blank=True),
        ),
    ]
