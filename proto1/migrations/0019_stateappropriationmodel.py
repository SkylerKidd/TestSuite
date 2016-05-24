# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto1', '0018_institutionmodel_nominal_time_to_graduate'),
    ]

    operations = [
        migrations.CreateModel(
            name='StateAppropriationModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.CharField(max_length=50)),
                ('academic_year', models.IntegerField()),
                ('institution', models.CharField(max_length=100)),
                ('appropriation', models.FloatField()),
            ],
        ),
    ]
