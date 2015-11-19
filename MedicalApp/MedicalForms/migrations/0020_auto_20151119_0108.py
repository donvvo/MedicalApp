# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0019_auto_20151119_0055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='healthhistory',
            old_name='woemn_only_choices',
            new_name='women_only_choices',
        ),
    ]
