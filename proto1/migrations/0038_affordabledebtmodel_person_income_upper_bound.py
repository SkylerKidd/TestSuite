# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto1', '0037_affordabledebtmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='affordabledebtmodel',
            name='person_income_upper_bound',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
