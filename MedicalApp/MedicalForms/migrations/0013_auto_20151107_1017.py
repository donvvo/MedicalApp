# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import MedicalForms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0012_auto_20151107_0350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientinformation',
            name='gender',
            field=MedicalForms.utils.MyCharField(blank=True, max_length=10, choices=[(b'Male', b'Male'), (b'Female', b'Female')]),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='name',
            field=MedicalForms.utils.MyCharField(max_length=100, blank=True),
        ),
    ]
