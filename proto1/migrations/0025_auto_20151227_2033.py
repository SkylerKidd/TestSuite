# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto1', '0024_auto_20151227_2031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pellgrantmodel',
            old_name='award',
            new_name='pell_award',
        ),
    ]
