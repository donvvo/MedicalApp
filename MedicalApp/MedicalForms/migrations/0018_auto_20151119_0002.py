# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import MedicalForms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalAppointments', '0010_auto_20151116_2112'),
        ('MedicalForms', '0017_accidenthistory_today_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientinformation',
            name='complete',
        ),
        migrations.RemoveField(
            model_name='patientinformation',
            name='user',
        ),
        migrations.AddField(
            model_name='patientinformation',
            name='patient',
            field=models.OneToOneField(primary_key=True, default=4, serialize=False, to='MedicalAppointments.Patient'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='accident_date',
            field=MedicalForms.utils.MyDateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='date_of_birth',
            field=MedicalForms.utils.MyDateTimeField(null=True, blank=True),
        ),
    ]
