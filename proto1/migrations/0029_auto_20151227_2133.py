# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto1', '0028_auto_20151227_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stateneedgrantdistributionschedulemodel',
            name='percent_of_max_award',
            field=models.FloatField(),
        ),
    ]
