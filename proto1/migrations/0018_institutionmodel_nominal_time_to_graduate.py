# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto1', '0017_auto_20151123_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='institutionmodel',
            name='nominal_time_to_graduate',
            field=models.FloatField(default=4.0),
            preserve_default=False,
        ),
    ]
