# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalAppointments', '0006_auto_20160107_2312'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewForms',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('new_form', models.FileField(upload_to=b'forms')),
                ('booking', models.ForeignKey(to='MedicalAppointments.Booking')),
            ],
        ),
    ]
