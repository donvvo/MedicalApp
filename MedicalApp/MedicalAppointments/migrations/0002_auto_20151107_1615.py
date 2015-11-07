# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalAppointments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='clinic',
            name='id',
        ),
        migrations.AlterField(
            model_name='clinic',
            name='name',
            field=models.CharField(max_length=100, serialize=False, primary_key=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='clinic',
            field=models.ForeignKey(to='MedicalAppointments.Clinic'),
        ),
        migrations.AddField(
            model_name='booking',
            name='doctor',
            field=models.ForeignKey(to='MedicalAppointments.Doctor'),
        ),
        migrations.AddField(
            model_name='booking',
            name='patient',
            field=models.ForeignKey(to='MedicalAppointments.Patient'),
        ),
    ]
