# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import MedicalForms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peripheraljointbasequestions',
            name='pain_location',
            field=MedicalForms.utils.MyCharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='peripheraljointbasequestions',
            name='radiation',
            field=MedicalForms.utils.MyNullBooleanField(),
        ),
    ]
