# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto1', '0019_stateappropriationmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nontuitioncostsmodel',
            old_name='food',
            new_name='books',
        ),
        migrations.RenameField(
            model_name='nontuitioncostsmodel',
            old_name='rent',
            new_name='miscellaneous',
        ),
        migrations.RenameField(
            model_name='nontuitioncostsmodel',
            old_name='stationary',
            new_name='room_and_board',
        ),
        migrations.RenameField(
            model_name='nontuitioncostsmodel',
            old_name='transport',
            new_name='transportation',
        ),
    ]
