# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0003_auto_20151126_1722'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tmjscreening',
            old_name='pain_description_5',
            new_name='pain_description_4',
        ),
        migrations.RenameField(
            model_name='tmjscreening',
            old_name='pain_level_5',
            new_name='pain_level_4',
        ),
    ]
