# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import MedicalForms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalAppointments', '0010_auto_20151116_2112'),
        ('MedicalForms', '0037_patientspecific'),
    ]

    operations = [
        migrations.CreateModel(
            name='DateSignature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('signature_date', MedicalForms.utils.MyDateTimeField(null=True, blank=True)),
                ('signature', MedicalForms.utils.MyCharField(max_length=50, blank=True)),
                ('patient', models.ForeignKey(to='MedicalAppointments.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='TreatmentPlan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('plan_name', MedicalForms.utils.MyCharField(max_length=50, blank=True)),
                ('approved', MedicalForms.utils.MyCharField(max_length=50, blank=True)),
                ('patient', models.ForeignKey(to='MedicalAppointments.Patient')),
            ],
        ),
    ]
