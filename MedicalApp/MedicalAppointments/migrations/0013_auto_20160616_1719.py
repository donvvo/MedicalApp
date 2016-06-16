# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import MedicalForms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalAppointments', '0012_auto_20160616_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='current_medications',
            field=MedicalForms.utils.MyCharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='past_medications',
            field=MedicalForms.utils.MyCharField(max_length=200, blank=True),
        ),
    ]
