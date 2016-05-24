# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def remove_99999_from_tuition_tables(apps, schema_editor):
    TuitionCostsModel = apps.get_model('proto1', 'TuitionCostsModel')
    TuitionCostsModel.objects.filter(tuition_and_fees=999999).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('proto1', '0038_affordabledebtmodel_person_income_upper_bound'),
    ]

    operations = [
        migrations.RunPython(remove_99999_from_tuition_tables)
    ]
