# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto1', '0008_auto_20151023_1001'),
    ]

    operations = [
        migrations.CreateModel(
            name='StateNeedGrantDistributionSchedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('academic_year', models.IntegerField()),
                ('lower_percent_median_income', models.IntegerField()),
                ('upper_percent_median_income', models.IntegerField()),
                ('percent_of_max_award', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StateNeedGrantMaxAward',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('academic_year', models.IntegerField()),
                ('institution_type', models.CharField(max_length=50, choices=[(b'Public research', b'Public research'), (b'Public regional', b'Public regional'), (b'CTC', b'Community College'), (b'Private nonprofits', b'Private nonprofits')])),
                ('max_award', models.IntegerField()),
            ],
        ),
    ]
