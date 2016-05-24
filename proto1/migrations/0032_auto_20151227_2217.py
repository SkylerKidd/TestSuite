# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto1', '0031_auto_20151227_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stateneedgrantmaxawardmodel',
            name='institution_type',
            field=models.CharField(max_length=50),
        ),
    ]
