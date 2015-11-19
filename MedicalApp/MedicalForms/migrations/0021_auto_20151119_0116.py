# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0020_auto_20151119_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthhistory',
            name='women_only_choices',
            field=models.ManyToManyField(to='MedicalForms.WomenOnlyChoices', blank=True),
        ),
    ]
