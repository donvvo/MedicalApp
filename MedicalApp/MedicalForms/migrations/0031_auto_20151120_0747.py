# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import MedicalForms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0030_auto_20151120_0731'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportoffindings',
            name='clinician_signature',
            field=MedicalForms.utils.MyCharField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='reportoffindings',
            name='patient_signature',
            field=MedicalForms.utils.MyCharField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='reportoffindings',
            name='signature_date',
            field=MedicalForms.utils.MyDateTimeField(null=True, blank=True),
        ),
    ]
