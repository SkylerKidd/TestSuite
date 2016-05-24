# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MedianFamilyIncome',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('income', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PovertyGuideline',
            fields=[
                ('year', models.IntegerField(serialize=False)),
                ('first_person', models.IntegerField()),
                ('each_additional_person', models.IntegerField()),
            ],
        ),
    ]
