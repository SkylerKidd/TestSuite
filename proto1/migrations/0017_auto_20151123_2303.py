# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto1', '0016_enrollment_institutionmodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Enrollment',
            new_name='EnrollmentModel',
        ),
    ]
