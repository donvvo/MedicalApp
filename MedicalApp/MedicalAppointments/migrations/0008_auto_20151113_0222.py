# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import MedicalForms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalAppointments', '0007_auto_20151112_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinic',
            name='address',
            field=MedicalForms.utils.MyCharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='clinic',
            name='city',
            field=MedicalForms.utils.MyCharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='clinic',
            name='description',
            field=MedicalForms.utils.MyTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='clinic',
            name='email',
            field=MedicalForms.utils.MyEmailField(max_length=254, blank=True),
        ),
        migrations.AlterField(
            model_name='clinic',
            name='end_time',
            field=MedicalForms.utils.MyCharField(max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='clinic',
            name='name',
            field=MedicalForms.utils.MyCharField(max_length=100, serialize=False, primary_key=True, blank=True),
        ),
        migrations.AlterField(
            model_name='clinic',
            name='phone',
            field=MedicalForms.utils.MyCharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='clinic',
            name='postal_code',
            field=MedicalForms.utils.MyCharField(max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='clinic',
            name='start_time',
            field=MedicalForms.utils.MyCharField(max_length=10, blank=True),
        ),
    ]
