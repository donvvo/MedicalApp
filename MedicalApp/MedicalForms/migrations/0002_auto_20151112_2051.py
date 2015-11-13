# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import MedicalForms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalAppointments', '0007_auto_20151112_1216'),
        ('MedicalForms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TMJScreening',
            fields=[
                ('patient', models.OneToOneField(primary_key=True, serialize=False, to='MedicalAppointments.Patient')),
                ('today_date', MedicalForms.utils.MyDateTimeField(auto_now_add=True, null=True)),
                ('signature', MedicalForms.utils.MyCharField(max_length=50, blank=True)),
                ('pain', models.ManyToManyField(to='MedicalForms.Pain', blank=True)),
                ('symptom', models.ManyToManyField(to='MedicalForms.Symptom', blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='accidenthistory',
            name='airbag_deployed',
            field=MedicalForms.utils.MyNullBooleanField(),
        ),
        migrations.AlterField(
            model_name='accidenthistory',
            name='anticipation_of_accident',
            field=MedicalForms.utils.MyNullBooleanField(),
        ),
        migrations.AlterField(
            model_name='accidenthistory',
            name='collision_type',
            field=MedicalForms.utils.MySelectField(max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='accidenthistory',
            name='description_and_location',
            field=MedicalForms.utils.MyTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='accidenthistory',
            name='dominant_hand',
            field=MedicalForms.utils.MySelectField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='accidenthistory',
            name='driver',
            field=MedicalForms.utils.MyNullBooleanField(),
        ),
        migrations.AlterField(
            model_name='accidenthistory',
            name='exit_from_vehicle',
            field=MedicalForms.utils.MySelectField(max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='accidenthistory',
            name='impact_with_objects',
            field=MedicalForms.utils.MyCharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='accidenthistory',
            name='loss_of_consciousness',
            field=MedicalForms.utils.MyNullBooleanField(),
        ),
        migrations.AlterField(
            model_name='accidenthistory',
            name='other_vehicle',
            field=MedicalForms.utils.MyCharField(max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='accidenthistory',
            name='other_vehicle_speed',
            field=MedicalForms.utils.MyIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='accidenthistory',
            name='patient_vehicle',
            field=MedicalForms.utils.MyCharField(max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='accidenthistory',
            name='patient_vehicle_speed',
            field=MedicalForms.utils.MyIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='accidenthistory',
            name='road_condition',
            field=MedicalForms.utils.MySelectField(max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='accidenthistory',
            name='safety_equipment',
            field=MedicalForms.utils.MyNullBooleanField(),
        ),
        migrations.AlterField(
            model_name='accidenthistory',
            name='time_of_the_day',
            field=MedicalForms.utils.MyDateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='accidenthistory',
            name='vehicle_towed',
            field=MedicalForms.utils.MyNullBooleanField(),
        ),
    ]
