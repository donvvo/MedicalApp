# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import MedicalForms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalAppointments', '0010_auto_20151116_2112'),
        ('MedicalForms', '0033_lowerextremity'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpperExtremity',
            fields=[
                ('patient', models.OneToOneField(primary_key=True, serialize=False, to='MedicalAppointments.Patient')),
                ('question_1', MedicalForms.utils.MyRadioField(max_length=2, blank=True)),
                ('question_2', MedicalForms.utils.MyRadioField(max_length=2, blank=True)),
                ('question_3', MedicalForms.utils.MyRadioField(max_length=2, blank=True)),
                ('question_4', MedicalForms.utils.MyRadioField(max_length=2, blank=True)),
                ('question_5', MedicalForms.utils.MyRadioField(max_length=2, blank=True)),
                ('question_6', MedicalForms.utils.MyRadioField(max_length=2, blank=True)),
                ('question_7', MedicalForms.utils.MyRadioField(max_length=2, blank=True)),
                ('question_8', MedicalForms.utils.MyRadioField(max_length=2, blank=True)),
                ('question_9', MedicalForms.utils.MyRadioField(max_length=2, blank=True)),
                ('question_10', MedicalForms.utils.MyRadioField(max_length=2, blank=True)),
                ('question_11', MedicalForms.utils.MyRadioField(max_length=2, blank=True)),
                ('question_12', MedicalForms.utils.MyRadioField(max_length=2, blank=True)),
                ('question_13', MedicalForms.utils.MyRadioField(max_length=2, blank=True)),
                ('question_14', MedicalForms.utils.MyRadioField(max_length=2, blank=True)),
                ('question_15', MedicalForms.utils.MyRadioField(max_length=2, blank=True)),
                ('question_16', MedicalForms.utils.MyRadioField(max_length=2, blank=True)),
                ('question_17', MedicalForms.utils.MyRadioField(max_length=2, blank=True)),
                ('question_18', MedicalForms.utils.MyRadioField(max_length=2, blank=True)),
                ('question_19', MedicalForms.utils.MyRadioField(max_length=2, blank=True)),
                ('question_20', MedicalForms.utils.MyRadioField(max_length=2, blank=True)),
                ('column_totals_0', MedicalForms.utils.MyIntegerField(null=True, blank=True)),
                ('column_totals_1', MedicalForms.utils.MyIntegerField(null=True, blank=True)),
                ('column_totals_2', MedicalForms.utils.MyIntegerField(null=True, blank=True)),
                ('column_totals_3', MedicalForms.utils.MyIntegerField(null=True, blank=True)),
                ('total_score', MedicalForms.utils.MyIntegerField(null=True, blank=True)),
            ],
        ),
    ]
