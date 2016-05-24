# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto1', '0002_pellgrants'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pellgrants',
            old_name='year',
            new_name='academic_year',
        ),
    ]
