# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipeds', '0004_auto_20160312_1836'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppropriationsModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('institution_id', models.IntegerField(db_index=True)),
                ('academic_year', models.IntegerField(db_index=True)),
                ('state_appropriation', models.IntegerField(db_index=True)),
                ('local_appropriation', models.IntegerField(db_index=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='appropriationsmodel',
            unique_together=set([('institution_id', 'academic_year')]),
        ),
    ]
