# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto1', '0006_remove_expectedfamilycontribution_expected_family_contribution'),
    ]

    operations = [
        migrations.AddField(
            model_name='expectedfamilycontribution',
            name='expected_family_contribution',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='expectedfamilycontribution',
            name='family_income',
            field=models.IntegerField(default=0),
        ),
    ]
