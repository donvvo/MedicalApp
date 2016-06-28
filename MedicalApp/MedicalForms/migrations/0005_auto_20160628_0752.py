# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import MedicalForms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0004_auto_20160628_0601'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientinformation',
            name='chest_abs_pain_level',
            field=MedicalForms.utils.IntegerRangeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='head_pain_level',
            field=MedicalForms.utils.IntegerRangeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='lower_back_pain_level',
            field=MedicalForms.utils.IntegerRangeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='lower_extremities_pain_level',
            field=MedicalForms.utils.IntegerRangeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='neck_pain_level',
            field=MedicalForms.utils.IntegerRangeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='upper_extremities_pain_level',
            field=MedicalForms.utils.IntegerRangeField(null=True, blank=True),
        ),
    ]
