# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto1', '0035_auto_20160105_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='povertyguidelinemodel',
            name='id',
            field=models.AutoField(default=None, serialize=False, primary_key=True),
        ),
    ]
