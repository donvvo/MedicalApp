# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0002_auto_20160627_2217'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientinformation',
            old_name='chest_abs_type',
            new_name='chest_abs_pain_type',
        ),
        migrations.RenameField(
            model_name='patientinformation',
            old_name='lower_back_type',
            new_name='lower_back_pain_type',
        ),
        migrations.RenameField(
            model_name='patientinformation',
            old_name='lower_extremities_type',
            new_name='lower_extremities_pain_type',
        ),
        migrations.RenameField(
            model_name='patientinformation',
            old_name='neck_type',
            new_name='neck_pain_type',
        ),
        migrations.RenameField(
            model_name='patientinformation',
            old_name='upper_extremities_type',
            new_name='upper_extremities_pain_type',
        ),
    ]
