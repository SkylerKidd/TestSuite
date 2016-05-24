# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto1', '0030_auto_20151227_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stateneedgrantmaxawardmodel',
            name='sng_max_award',
            field=models.FloatField(),
        ),
    ]
