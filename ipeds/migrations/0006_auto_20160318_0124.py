# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipeds', '0005_auto_20160318_0058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appropriationsmodel',
            old_name='academic_year',
            new_name='fiscal_year',
        ),
        migrations.AlterUniqueTogether(
            name='appropriationsmodel',
            unique_together=set([('institution_id', 'fiscal_year')]),
        ),
    ]
