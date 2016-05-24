# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PellGrants',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cost_of_attendance_lower', models.IntegerField()),
                ('cost_of_attendance_upper', models.IntegerField()),
                ('expected_family_contribution_lower', models.IntegerField()),
                ('expected_family_contribution_upper', models.IntegerField()),
                ('year', models.IntegerField()),
                ('award', models.IntegerField()),
            ],
        ),
    ]
