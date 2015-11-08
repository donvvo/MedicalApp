# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalAppointments', '0004_auto_20151107_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='clinic',
            field=models.ForeignKey(to='MedicalAppointments.Clinic', blank=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialty',
            field=models.ForeignKey(to='MedicalAppointments.DoctorSpecialty', blank=True),
        ),
    ]
