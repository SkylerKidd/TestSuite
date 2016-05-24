# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto1', '0032_auto_20151227_2217'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tuitioncostsmodel',
            old_name='tuition',
            new_name='tuition_and_fees',
        ),
    ]
