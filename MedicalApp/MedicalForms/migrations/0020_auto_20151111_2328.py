# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0019_reportoffindings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportoffindings',
            name='date_of_assessment',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
