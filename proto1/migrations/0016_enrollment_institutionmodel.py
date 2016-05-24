# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto1', '0015_tuitioncostsmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.CharField(max_length=50)),
                ('institution', models.CharField(max_length=100)),
                ('academic_year', models.IntegerField()),
                ('fte_enrollment', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='InstitutionModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.CharField(max_length=50)),
                ('institution', models.CharField(max_length=100)),
                ('institution_type', models.CharField(max_length=50)),
            ],
        ),
    ]
