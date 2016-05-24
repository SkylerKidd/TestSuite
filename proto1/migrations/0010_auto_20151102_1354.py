# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto1', '0009_stateneedgrantdistributionschedule_stateneedgrantmaxaward'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PovertyGuideline',
            new_name='PovertyGuidelineModel',
        ),
    ]
