# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def remove_99999_from_tuition_tables(apps, schema_editor):
    TuitionCostsModel = apps.get_model('v2', 'TuitionCostsModel')
    TuitionCostsModel.objects.filter(tuition_and_fees=999999).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('v2', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(remove_99999_from_tuition_tables)
    ]
