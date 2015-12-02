# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalAppointments', '0002_clinic_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clinic',
            name='email',
        ),
    ]
