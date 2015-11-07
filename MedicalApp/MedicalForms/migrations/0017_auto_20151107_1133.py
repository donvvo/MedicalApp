# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import MedicalForms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0016_auto_20151107_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientinformation',
            name='job_requirements',
            field=MedicalForms.utils.MySelectField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='marital_status',
            field=MedicalForms.utils.MySelectField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='number_of_children',
            field=MedicalForms.utils.IntegerRangeField(blank=True),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='occupational_status',
            field=MedicalForms.utils.MySelectField(max_length=20, blank=True),
        ),
    ]
