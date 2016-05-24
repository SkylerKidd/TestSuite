# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto1', '0011_auto_20151102_1354'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ExpectedFamilyContribution',
            new_name='ExpectedFamilyContributionModel',
        ),
        migrations.RenameModel(
            old_name='PellGrant',
            new_name='PellGrantModel',
        ),
        migrations.RenameModel(
            old_name='StateNeedGrantDistributionSchedule',
            new_name='StateNeedGrantDistributionScheduleModel',
        ),
        migrations.RenameModel(
            old_name='StateNeedGrantMaxAward',
            new_name='StateNeedGrantMaxAwardModel',
        ),
    ]
