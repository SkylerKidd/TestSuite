# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto1', '0013_minimumwagemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='NonTuitionCostsModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('academic_year', models.IntegerField()),
                ('state', models.CharField(max_length=50)),
                ('living_status', models.CharField(max_length=100)),
                ('stationary', models.FloatField()),
                ('rent', models.FloatField()),
                ('transport', models.FloatField()),
                ('food', models.FloatField()),
            ],
        ),
    ]
