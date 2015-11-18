# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import MedicalForms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalAppointments', '0010_auto_20151116_2112'),
        ('MedicalForms', '0008_auto_20151113_0209'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChiropracticTreatment',
            fields=[
                ('patient', models.OneToOneField(primary_key=True, serialize=False, to='MedicalAppointments.Patient')),
                ('signature', MedicalForms.utils.MyCharField(max_length=50, blank=True)),
                ('date', MedicalForms.utils.MyDateTimeField(null=True, blank=True)),
                ('name', MedicalForms.utils.MyCharField(max_length=50, blank=True)),
            ],
        ),
    ]
