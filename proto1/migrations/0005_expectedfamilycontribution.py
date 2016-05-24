# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto1', '0004_auto_20151023_0614'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpectedFamilyContribution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('expected_family_contribution', models.IntegerField()),
            ],
        ),
    ]
