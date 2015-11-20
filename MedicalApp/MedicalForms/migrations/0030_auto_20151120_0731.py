# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import MedicalForms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0029_auto_20151120_0424'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportoffindings',
            name='id',
        ),
        migrations.AlterField(
            model_name='reportoffindings',
            name='date_of_assessment',
            field=MedicalForms.utils.MyDateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='reportoffindings',
            name='patient',
            field=models.OneToOneField(primary_key=True, serialize=False, to='MedicalAppointments.Patient'),
        ),
    ]
