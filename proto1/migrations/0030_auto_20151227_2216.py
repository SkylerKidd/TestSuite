# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto1', '0029_auto_20151227_2133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stateneedgrantmaxawardmodel',
            old_name='max_award',
            new_name='sng_max_award',
        ),
    ]
