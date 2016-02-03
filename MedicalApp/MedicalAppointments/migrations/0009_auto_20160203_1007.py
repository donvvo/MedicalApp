# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalAppointments', '0008_newforms_date_added'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newforms',
            name='booking',
        ),
        migrations.AddField(
            model_name='newforms',
            name='patient',
            field=models.ForeignKey(default=5, to='MedicalAppointments.Patient'),
            preserve_default=False,
        ),
    ]
