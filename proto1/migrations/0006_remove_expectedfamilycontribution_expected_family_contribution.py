# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto1', '0005_expectedfamilycontribution'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expectedfamilycontribution',
            name='expected_family_contribution',
        ),
    ]
