# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import MedicalForms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalAppointments', '0010_auto_20151116_2112'),
        ('MedicalForms', '0010_physiotherapytreatment'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeInformation',
            fields=[
                ('patient', models.OneToOneField(primary_key=True, serialize=False, to='MedicalAppointments.Patient')),
                ('physician_name', MedicalForms.utils.MyCharField(max_length=50, blank=True)),
                ('physician_address', MedicalForms.utils.MyCharField(max_length=50, blank=True)),
                ('physician_phone', MedicalForms.utils.MyCharField(max_length=50, blank=True)),
                ('physician_fax', MedicalForms.utils.MyCharField(max_length=50, blank=True)),
                ('patient_name', MedicalForms.utils.MyCharField(max_length=50, blank=True)),
                ('patient_dob', MedicalForms.utils.MyCharField(max_length=50, blank=True)),
                ('representative_name1', MedicalForms.utils.MyCharField(max_length=50, blank=True)),
                ('forward_from_name', MedicalForms.utils.MyCharField(max_length=50, blank=True)),
                ('include_notes', MedicalForms.utils.MyNullBooleanField()),
                ('signature', MedicalForms.utils.MyCharField(max_length=50, blank=True)),
                ('representative_name2', MedicalForms.utils.MyCharField(max_length=50, blank=True)),
                ('representative_relationship', MedicalForms.utils.MyCharField(max_length=50, blank=True)),
                ('TO', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('RE', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('date', MedicalForms.utils.MyDateTimeField(null=True, blank=True)),
                ('patient_signature', MedicalForms.utils.MyCharField(max_length=50, blank=True)),
                ('witness_signature', MedicalForms.utils.MyCharField(max_length=50, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='MassageTreatment',
            fields=[
                ('patient', models.OneToOneField(primary_key=True, serialize=False, to='MedicalAppointments.Patient')),
                ('signature', MedicalForms.utils.MyCharField(max_length=50, blank=True)),
                ('date', MedicalForms.utils.MyDateTimeField(null=True, blank=True)),
                ('name', MedicalForms.utils.MyCharField(max_length=50, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalAuthorization',
            fields=[
                ('patient', models.OneToOneField(primary_key=True, serialize=False, to='MedicalAppointments.Patient')),
                ('TO', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('RE', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('date', MedicalForms.utils.MyDateTimeField(null=True, blank=True)),
                ('patient_signature', MedicalForms.utils.MyCharField(max_length=50, blank=True)),
                ('witness_signature', MedicalForms.utils.MyCharField(max_length=50, blank=True)),
            ],
        ),
    ]
