# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto1', '0014_nontuitioncostsmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='TuitionCostsModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('academic_year', models.IntegerField()),
                ('state', models.CharField(max_length=50)),
                ('institution', models.CharField(max_length=100)),
                ('tuition', models.FloatField()),
            ],
        ),
    ]
