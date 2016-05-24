# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto1', '0022_auto_20151227_2026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pellgrantmodel',
            old_name='expected_family_contribution_lower',
            new_name='efc_lower',
        ),
    ]
