# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto1', '0012_auto_20151102_1359'),
    ]

    operations = [
        migrations.CreateModel(
            name='MinimumWageModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('calendar_year', models.IntegerField()),
                ('state', models.CharField(max_length=50)),
                ('minimum_wage', models.FloatField()),
            ],
        ),
    ]
