# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import MedicalForms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalAppointments', '0013_auto_20160616_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='alcohol',
            field=MedicalForms.utils.MyNullBooleanField(),
        ),
        migrations.AddField(
            model_name='patient',
            name='height',
            field=MedicalForms.utils.MyCharField(max_length=30, blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='marijuana',
            field=MedicalForms.utils.MyNullBooleanField(),
        ),
        migrations.AddField(
            model_name='patient',
            name='smoking',
            field=MedicalForms.utils.MyNullBooleanField(),
        ),
        migrations.AddField(
            model_name='patient',
            name='weight',
            field=MedicalForms.utils.MyCharField(max_length=30, blank=True),
        ),
    ]
