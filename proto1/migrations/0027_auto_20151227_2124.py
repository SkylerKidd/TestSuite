# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto1', '0026_auto_20151227_2119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stateappropriationmodel',
            old_name='academic_year',
            new_name='fiscal_year',
        ),
    ]
