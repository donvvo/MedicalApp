# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import MedicalForms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalAppointments', '0010_auto_20151116_2112'),
        ('MedicalForms', '0036_neckdisability'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientSpecific',
            fields=[
                ('patient', models.OneToOneField(primary_key=True, serialize=False, to='MedicalAppointments.Patient')),
                ('date_1', MedicalForms.utils.MyDateTimeField(null=True, blank=True)),
                ('date_2', MedicalForms.utils.MyDateTimeField(null=True, blank=True)),
                ('date_3', MedicalForms.utils.MyDateTimeField(null=True, blank=True)),
                ('date_4', MedicalForms.utils.MyDateTimeField(null=True, blank=True)),
                ('date_5', MedicalForms.utils.MyDateTimeField(null=True, blank=True)),
                ('activity_1', MedicalForms.utils.MyCharField(max_length=20, blank=True)),
                ('score_1_1', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('score_1_2', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('score_1_3', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('score_1_4', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('score_1_5', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('score_1_6', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('activity_2', MedicalForms.utils.MyCharField(max_length=20, blank=True)),
                ('score_2_1', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('score_2_2', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('score_2_3', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('score_2_4', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('score_2_5', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('score_2_6', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('activity_3', MedicalForms.utils.MyCharField(max_length=20, blank=True)),
                ('score_3_1', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('score_3_2', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('score_3_3', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('score_3_4', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('score_3_5', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('score_3_6', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('activity_4', MedicalForms.utils.MyCharField(max_length=20, blank=True)),
                ('score_4_1', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('score_4_2', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('score_4_3', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('score_4_4', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('score_4_5', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('score_4_6', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('activity_5', MedicalForms.utils.MyCharField(max_length=20, blank=True)),
                ('score_5_1', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('score_5_2', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('score_5_3', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('score_5_4', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('score_5_5', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('score_5_6', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('score_additional_1', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('score_additional_2', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('score_additional_3', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('score_additional_4', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('score_additional_5', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('score_additional_6', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('score_average_1', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('score_average_2', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('score_average_3', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('score_average_4', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('score_average_5', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('score_average_6', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
            ],
        ),
    ]
