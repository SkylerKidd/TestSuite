# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipeds', '0003_auto_20160311_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnrollmentModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('institution_id', models.IntegerField(db_index=True)),
                ('estimated_fte_undergraduate', models.IntegerField(default=None, null=True, blank=True)),
                ('reported_fte_undergraduate', models.IntegerField(default=None, null=True, blank=True)),
                ('academic_year', models.IntegerField(db_index=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='institutionmodel',
            unique_together=set([('institution_id', 'academic_year')]),
        ),
        migrations.AlterUniqueTogether(
            name='enrollmentmodel',
            unique_together=set([('institution_id', 'academic_year')]),
        ),
    ]
