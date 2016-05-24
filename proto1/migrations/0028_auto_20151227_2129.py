# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto1', '0027_auto_20151227_2124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stateneedgrantdistributionschedulemodel',
            old_name='lower_percent_median_income',
            new_name='percent_mfi_lower',
        ),
        migrations.RenameField(
            model_name='stateneedgrantdistributionschedulemodel',
            old_name='upper_percent_median_income',
            new_name='percent_mfi_upper',
        ),
    ]
