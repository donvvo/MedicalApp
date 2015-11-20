# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import MedicalForms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0024_dischargereasons_patientdischarge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accidenthistory',
            name='impact_with_objects',
        ),
        migrations.AddField(
            model_name='accidenthistory',
            name='impact_with_objects_boolean',
            field=MedicalForms.utils.MyNullBooleanField(),
        ),
        migrations.AddField(
            model_name='accidenthistory',
            name='impact_with_objects_detail',
            field=MedicalForms.utils.MyCharField(max_length=50, blank=True),
        ),
    ]
