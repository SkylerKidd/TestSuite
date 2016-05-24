# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto1', '0010_auto_20151102_1354'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MedianFamilyIncome',
            new_name='MedianFamilyIncomeModel',
        ),
    ]
