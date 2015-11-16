# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalAppointments', '0008_auto_20151113_0222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='clinic',
            field=models.ForeignKey(blank=True, to='MedicalAppointments.Clinic', null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialty',
            field=models.ForeignKey(blank=True, to='MedicalAppointments.DoctorSpecialty', null=True),
        ),
    ]
