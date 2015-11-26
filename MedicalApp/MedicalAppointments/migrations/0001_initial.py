# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings
import MedicalForms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20151107_0557'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('name', MedicalForms.utils.MyCharField(max_length=100, serialize=False, primary_key=True)),
                ('phone', MedicalForms.utils.MyCharField(max_length=20, blank=True)),
                ('email', MedicalForms.utils.MyEmailField(max_length=254, blank=True)),
                ('description', MedicalForms.utils.MyTextField(blank=True)),
                ('city', MedicalForms.utils.MyCharField(max_length=20, blank=True)),
                ('address', MedicalForms.utils.MyCharField(max_length=200, blank=True)),
                ('postal_code', MedicalForms.utils.MyCharField(max_length=10, blank=True)),
                ('start_time_mon', MedicalForms.utils.MyTimeField(null=True, blank=True)),
                ('end_time_mon', MedicalForms.utils.MyTimeField(null=True, blank=True)),
                ('start_time_tue', MedicalForms.utils.MyTimeField(null=True, blank=True)),
                ('end_time_tue', MedicalForms.utils.MyTimeField(null=True, blank=True)),
                ('start_time_wed', MedicalForms.utils.MyTimeField(null=True, blank=True)),
                ('end_time_wed', MedicalForms.utils.MyTimeField(null=True, blank=True)),
                ('start_time_thurs', MedicalForms.utils.MyTimeField(null=True, blank=True)),
                ('end_time_thurs', MedicalForms.utils.MyTimeField(null=True, blank=True)),
                ('start_time_fri', MedicalForms.utils.MyTimeField(null=True, blank=True)),
                ('end_time_fri', MedicalForms.utils.MyTimeField(null=True, blank=True)),
                ('start_time_sat', MedicalForms.utils.MyTimeField(null=True, blank=True)),
                ('end_time_sat', MedicalForms.utils.MyTimeField(null=True, blank=True)),
                ('start_time_sun', MedicalForms.utils.MyTimeField(null=True, blank=True)),
                ('end_time_sun', MedicalForms.utils.MyTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='MedicalAppointments.Clinic', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DoctorSpecialty',
            fields=[
                ('specialty', models.CharField(max_length=20, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='specialty',
            field=models.ForeignKey(blank=True, to='MedicalAppointments.DoctorSpecialty', null=True),
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
