# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto1', '0020_auto_20151227_1954'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pellgrantmodel',
            old_name='cost_of_attendance_lower',
            new_name='coa_lower',
        ),
    ]
