# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto1', '0034_grantsscholarshipsmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='povertyguidelinemodel',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=None, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='enrollmentmodel',
            name='academic_year',
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='enrollmentmodel',
            name='state',
            field=models.CharField(max_length=50, db_index=True),
        ),
        migrations.AlterField(
            model_name='grantsscholarshipsmodel',
            name='academic_year',
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='grantsscholarshipsmodel',
            name='dependency_status',
            field=models.CharField(max_length=100, db_index=True),
        ),
        migrations.AlterField(
            model_name='grantsscholarshipsmodel',
            name='institution_type',
            field=models.CharField(max_length=50, db_index=True),
        ),
        migrations.AlterField(
            model_name='grantsscholarshipsmodel',
            name='state',
            field=models.CharField(max_length=50, db_index=True),
        ),
        migrations.AlterField(
            model_name='institutionmodel',
            name='institution_type',
            field=models.CharField(max_length=50, db_index=True),
        ),
        migrations.AlterField(
            model_name='institutionmodel',
            name='state',
            field=models.CharField(max_length=50, db_index=True),
        ),
        migrations.AlterField(
            model_name='medianfamilyincomemodel',
            name='state',
            field=models.CharField(max_length=50, db_index=True),
        ),
        migrations.AlterField(
            model_name='medianfamilyincomemodel',
            name='year',
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='minimumwagemodel',
            name='calendar_year',
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='minimumwagemodel',
            name='state',
            field=models.CharField(max_length=50, db_index=True),
        ),
        migrations.AlterField(
            model_name='nontuitioncostsmodel',
            name='academic_year',
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='nontuitioncostsmodel',
            name='living_status',
            field=models.CharField(max_length=100, db_index=True),
        ),
        migrations.AlterField(
            model_name='nontuitioncostsmodel',
            name='state',
            field=models.CharField(max_length=50, db_index=True),
        ),
        migrations.AlterField(
            model_name='pellgrantmodel',
            name='academic_year',
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='povertyguidelinemodel',
            name='year',
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='stateappropriationmodel',
            name='fiscal_year',
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='stateneedgrantdistributionschedulemodel',
            name='academic_year',
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='stateneedgrantmaxawardmodel',
            name='academic_year',
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='stateneedgrantmaxawardmodel',
            name='institution_type',
            field=models.CharField(max_length=50, db_index=True),
        ),
        migrations.AlterField(
            model_name='tuitioncostsmodel',
            name='academic_year',
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='tuitioncostsmodel',
            name='institution',
            field=models.CharField(max_length=100, db_index=True),
        ),
        migrations.AlterField(
            model_name='tuitioncostsmodel',
            name='state',
            field=models.CharField(max_length=50, db_index=True),
        ),
    ]
