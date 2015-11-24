# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import MedicalForms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalAppointments', '0010_auto_20151116_2112'),
        ('MedicalForms', '0035_auto_20151123_2111'),
    ]

    operations = [
        migrations.CreateModel(
            name='NeckDisability',
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
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
