# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto1', '0003_auto_20151023_0613'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PellGrants',
            new_name='PellGrant',
        ),
    ]
