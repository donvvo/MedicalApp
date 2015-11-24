# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0034_upperextremity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lowerextremity',
            name='column_totals',
        ),
        migrations.RemoveField(
            model_name='upperextremity',
            name='column_totals_0',
        ),
        migrations.RemoveField(
            model_name='upperextremity',
            name='column_totals_1',
        ),
        migrations.RemoveField(
            model_name='upperextremity',
            name='column_totals_2',
        ),
        migrations.RemoveField(
            model_name='upperextremity',
            name='column_totals_3',
        ),
        migrations.RemoveField(
            model_name='upperextremity',
            name='total_score',
        ),
    ]
