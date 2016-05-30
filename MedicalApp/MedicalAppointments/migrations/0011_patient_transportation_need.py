# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import MedicalForms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalAppointments', '0010_doctorspecialty_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='transportation_need',
            field=MedicalForms.utils.MySelectField(default=b'Regular', max_length=30, blank=True),
        ),
    ]
