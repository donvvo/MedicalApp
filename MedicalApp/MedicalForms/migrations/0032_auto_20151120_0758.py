# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0031_auto_20151120_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportoffindings',
            name='doctor',
            field=models.OneToOneField(to='MedicalAppointments.Doctor'),
        ),
    ]
