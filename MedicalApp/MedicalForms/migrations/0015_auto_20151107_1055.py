# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import MedicalForms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0014_auto_20151107_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientinformation',
            name='address',
            field=MedicalForms.utils.MyCharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='city',
            field=MedicalForms.utils.MyCharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='emergency_contact_name',
            field=MedicalForms.utils.MyCharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='emergency_contact_phone',
            field=MedicalForms.utils.MyCharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='emergency_contact_relationship',
            field=MedicalForms.utils.MyCharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='first_language',
            field=MedicalForms.utils.MyCharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='home_phone',
            field=MedicalForms.utils.MyCharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='mobile_phone',
            field=MedicalForms.utils.MyCharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='occupation',
            field=MedicalForms.utils.MyCharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='postal_code',
            field=MedicalForms.utils.MyCharField(max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='work_phone',
            field=MedicalForms.utils.MyCharField(max_length=20, blank=True),
        ),
    ]
