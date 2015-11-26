# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import MedicalForms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0002_auto_20151126_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='tmjscreening',
            name='pain_description_1',
            field=MedicalForms.utils.MySelectField(max_length=10, blank=True),
        ),
        migrations.AddField(
            model_name='tmjscreening',
            name='pain_description_2',
            field=MedicalForms.utils.MySelectField(max_length=10, blank=True),
        ),
        migrations.AddField(
            model_name='tmjscreening',
            name='pain_description_3',
            field=MedicalForms.utils.MySelectField(max_length=10, blank=True),
        ),
        migrations.AddField(
            model_name='tmjscreening',
            name='pain_description_5',
            field=MedicalForms.utils.MySelectField(max_length=10, blank=True),
        ),
        migrations.AddField(
            model_name='tmjscreening',
            name='pain_intensity',
            field=MedicalForms.utils.MyRadioField(max_length=2, blank=True),
        ),
        migrations.AddField(
            model_name='tmjscreening',
            name='pain_level_1',
            field=MedicalForms.utils.MySelectField(max_length=10, blank=True),
        ),
        migrations.AddField(
            model_name='tmjscreening',
            name='pain_level_2',
            field=MedicalForms.utils.MySelectField(max_length=10, blank=True),
        ),
        migrations.AddField(
            model_name='tmjscreening',
            name='pain_level_3',
            field=MedicalForms.utils.MySelectField(max_length=10, blank=True),
        ),
        migrations.AddField(
            model_name='tmjscreening',
            name='pain_level_5',
            field=MedicalForms.utils.MySelectField(max_length=10, blank=True),
        ),
    ]
