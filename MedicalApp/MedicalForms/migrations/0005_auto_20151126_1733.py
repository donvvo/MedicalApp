# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import MedicalForms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0004_auto_20151126_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tmjscreening',
            name='pain_description_1',
            field=MedicalForms.utils.MySelectField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='tmjscreening',
            name='pain_description_2',
            field=MedicalForms.utils.MySelectField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='tmjscreening',
            name='pain_description_3',
            field=MedicalForms.utils.MySelectField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='tmjscreening',
            name='pain_description_4',
            field=MedicalForms.utils.MySelectField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='tmjscreening',
            name='pain_level_1',
            field=MedicalForms.utils.MySelectField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='tmjscreening',
            name='pain_level_2',
            field=MedicalForms.utils.MySelectField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='tmjscreening',
            name='pain_level_3',
            field=MedicalForms.utils.MySelectField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='tmjscreening',
            name='pain_level_4',
            field=MedicalForms.utils.MySelectField(max_length=20, blank=True),
        ),
    ]
