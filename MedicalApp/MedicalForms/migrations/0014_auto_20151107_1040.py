# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0013_auto_20151107_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientinformation',
            name='gender',
            field=models.CharField(blank=True, max_length=10, choices=[(b'Male', b'Male'), (b'Female', b'Female')]),
        ),
    ]
