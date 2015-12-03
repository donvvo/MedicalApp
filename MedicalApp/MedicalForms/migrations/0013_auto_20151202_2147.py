# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0012_auto_20151202_2145'),
    ]

    operations = [
        migrations.RenameField(
            model_name='acuteconcussionevaluation',
            old_name='dignosis',
            new_name='diagnosis',
        ),
    ]
