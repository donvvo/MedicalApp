# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import MedicalForms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0021_auto_20151112_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthhistory',
            name='cnd_disorders',
            field=MedicalForms.utils.MyCharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='healthhistory',
            name='current_medications',
            field=MedicalForms.utils.MyTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='healthhistory',
            name='family_doctor',
            field=MedicalForms.utils.MyCharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='healthhistory',
            name='family_doctor_telephone',
            field=MedicalForms.utils.MyCharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='healthhistory',
            name='menstrual_flow',
            field=MedicalForms.utils.MySelectField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='healthhistory',
            name='other_conditions',
            field=MedicalForms.utils.MyTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='healthhistory',
            name='pregnant',
            field=MedicalForms.utils.MyNullBooleanField(),
        ),
        migrations.AlterField(
            model_name='healthhistory',
            name='previous_surgeries',
            field=MedicalForms.utils.MyTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='healthhistory',
            name='smoker',
            field=MedicalForms.utils.MyNullBooleanField(),
        ),
    ]
