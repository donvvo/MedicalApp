# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import MedicalForms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0020_auto_20151111_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientinformation',
            name='current_complaint_1',
            field=MedicalForms.utils.MyCharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='current_complaint_2',
            field=MedicalForms.utils.MyCharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='current_complaint_3',
            field=MedicalForms.utils.MyCharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='current_complaint_4',
            field=MedicalForms.utils.MyCharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='hospitalized',
            field=MedicalForms.utils.MyNullBooleanField(),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='hospitalized_detail',
            field=MedicalForms.utils.MyCharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='previous_injury',
            field=MedicalForms.utils.MyNullBooleanField(),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='previous_injury_detail',
            field=MedicalForms.utils.MyCharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='previous_sporting_injury',
            field=MedicalForms.utils.MyNullBooleanField(),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='previous_sporting_injury_detail',
            field=MedicalForms.utils.MyCharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='previous_test',
            field=MedicalForms.utils.MyNullBooleanField(),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='previous_test_detail',
            field=MedicalForms.utils.MyCharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='previous_therapy',
            field=MedicalForms.utils.MyNullBooleanField(),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='previous_therapy_detail',
            field=MedicalForms.utils.MyCharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='previous_work_injury',
            field=MedicalForms.utils.MyNullBooleanField(),
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='previous_work_injury_detail',
            field=MedicalForms.utils.MyCharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='modified_duties_availability',
            field=MedicalForms.utils.MyNullBooleanField(),
        ),
    ]
