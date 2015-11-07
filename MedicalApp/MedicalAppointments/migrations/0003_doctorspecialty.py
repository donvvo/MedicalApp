# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalAppointments', '0002_auto_20151107_1615'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorSpecialty',
            fields=[
                ('specialty', models.CharField(max_length=20, serialize=False, primary_key=True)),
            ],
        ),
    ]
