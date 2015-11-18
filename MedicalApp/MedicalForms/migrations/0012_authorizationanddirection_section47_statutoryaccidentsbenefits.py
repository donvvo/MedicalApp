# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import MedicalForms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalAppointments', '0010_auto_20151116_2112'),
        ('MedicalForms', '0011_exchangeinformation_massagetreatment_medicalauthorization'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorizationAndDirection',
            fields=[
                ('patient', models.OneToOneField(primary_key=True, serialize=False, to='MedicalAppointments.Patient')),
                ('TO', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('FROM', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('patient_name', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('automobile_insurer', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('claim_policy_number', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('date_of_loss', MedicalForms.utils.MyDateTimeField(null=True, blank=True)),
                ('SIN', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('legal_representative', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('primary_insurer', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('authorize_name', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('date', MedicalForms.utils.MyDateTimeField(null=True, blank=True)),
                ('patient_signature', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('witness_name', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('witness_signature', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Section47',
            fields=[
                ('patient', models.OneToOneField(primary_key=True, serialize=False, to='MedicalAppointments.Patient')),
                ('date', MedicalForms.utils.MyDateTimeField(null=True, blank=True)),
                ('patient_name', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('patient_signature', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('witness_name', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('witness_signature', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='StatutoryAccidentsBenefits',
            fields=[
                ('patient', models.OneToOneField(primary_key=True, serialize=False, to='MedicalAppointments.Patient')),
                ('date', MedicalForms.utils.MyDateTimeField(null=True, blank=True)),
                ('patient_name', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('patient_signature', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('witness_name', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('witness_signature', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
            ],
        ),
    ]
