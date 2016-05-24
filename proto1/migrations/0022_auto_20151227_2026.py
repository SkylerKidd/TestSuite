# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto1', '0021_auto_20151227_2023'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pellgrantmodel',
            old_name='cost_of_attendance_upper',
            new_name='coa_upper',
        ),
    ]
