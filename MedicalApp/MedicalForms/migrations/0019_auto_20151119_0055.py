# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalAppointments', '0010_auto_20151116_2112'),
        ('MedicalForms', '0018_auto_20151119_0002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='healthhistory',
            name='id',
        ),
        migrations.RemoveField(
            model_name='healthhistory',
            name='user',
        ),
        migrations.AddField(
            model_name='healthhistory',
            name='patient',
            field=models.OneToOneField(primary_key=True, default=4, serialize=False, to='MedicalAppointments.Patient'),
            preserve_default=False,
        ),
    ]
