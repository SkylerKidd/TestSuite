# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipeds', '0007_tuitionmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='NonTuitionModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('academic_year', models.IntegerField(db_index=True)),
                ('institution_id', models.IntegerField(db_index=True)),
                ('books', models.IntegerField(default=None, null=True, blank=True)),
                ('room_and_board_on_campus', models.IntegerField(default=None, null=True, blank=True)),
                ('transportation_and_misc_on_campus', models.IntegerField(default=None, null=True, blank=True)),
                ('room_and_board_off_campus_not_with_family', models.IntegerField(default=None, null=True, blank=True)),
                ('transportation_and_misc_off_campus_not_with_family', models.IntegerField(default=None, null=True, blank=True)),
                ('transportation_and_misc_off_campus_with_family', models.IntegerField(default=None, null=True, blank=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='tuitionmodel',
            unique_together=set([('institution_id', 'academic_year')]),
        ),
        migrations.AlterUniqueTogether(
            name='nontuitionmodel',
            unique_together=set([('institution_id', 'academic_year')]),
        ),
    ]
