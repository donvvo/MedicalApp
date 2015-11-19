# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalAppointments', '0010_auto_20151116_2112'),
        ('MedicalForms', '0012_authorizationanddirection_section47_statutoryaccidentsbenefits'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accidenthistory',
            name='id',
        ),
        migrations.RemoveField(
            model_name='accidenthistory',
            name='user',
        ),
        migrations.AddField(
            model_name='accidenthistory',
            name='patient',
            field=models.OneToOneField(primary_key=True, default=4, serialize=False, to='MedicalAppointments.Patient'),
            preserve_default=False,
        ),
    ]
