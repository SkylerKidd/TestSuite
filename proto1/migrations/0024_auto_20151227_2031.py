# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto1', '0023_auto_20151227_2028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pellgrantmodel',
            old_name='expected_family_contribution_upper',
            new_name='efc_upper',
        ),
    ]
