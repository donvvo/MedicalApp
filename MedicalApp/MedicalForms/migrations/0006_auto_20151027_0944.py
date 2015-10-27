# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MedicalForms', '0005_auto_20151025_2208'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccidentHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description_and_location', models.TextField(blank=True)),
                ('road_condition', models.CharField(blank=True, max_length=10, choices=[(b'Dry', b'Dry'), (b'Wet/Rainy', b'Wet/Rainy'), (b'Snow', b'Snow')])),
                ('anticipation_of_accident', models.NullBooleanField()),
                ('time_of_the_day', models.DateTimeField(blank=True)),
                ('patient_vehicle', models.CharField(max_length=30, blank=True)),
                ('patient_vehicle_speed', models.IntegerField(blank=True)),
                ('other_vehicle', models.CharField(max_length=30, blank=True)),
                ('other_vehicle_speed', models.IntegerField(blank=True)),
                ('collision_type', models.CharField(blank=True, max_length=30, choices=[(b'Front-End', b'Front-End'), (b'Side-End', b'Side-End'), (b'Side-Swipe', b'Side-Swipe'), (b'Rear-End', b'Rear-End')])),
                ('vehicle_towed', models.NullBooleanField()),
                ('impact_with_objects', models.CharField(max_length=50, blank=True)),
                ('exit_from_vehicle', models.CharField(blank=True, max_length=30, choices=[(b'Self-powered', b'Self-powered'), (b'Required Assistance', b'Required Assistance')])),
                ('loss_of_consciousness', models.NullBooleanField()),
                ('safety_equipment', models.NullBooleanField()),
                ('airbag_deployed', models.NullBooleanField()),
                ('driver', models.NullBooleanField()),
                ('dominant_hand', models.CharField(blank=True, max_length=20, choices=[(b'Left', b'Left'), (b'Right', b'Right')])),
            ],
        ),
        migrations.CreateModel(
            name='BodyPart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PassengerLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PatientInformation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('today_date', models.DateTimeField(auto_now_add=True)),
                ('accident_date', models.DateTimeField(blank=True)),
                ('date_of_birth', models.DateTimeField(blank=True)),
                ('name', models.CharField(max_length=100, blank=True)),
                ('gender', models.CharField(blank=True, max_length=10, choices=[(b'Male', b'Male'), (b'Female', b'Female')])),
                ('address', models.CharField(max_length=200, blank=True)),
                ('city', models.CharField(max_length=100, blank=True)),
                ('postal_code', models.CharField(max_length=10, blank=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('first_language', models.CharField(max_length=100, blank=True)),
                ('home_phone', models.CharField(max_length=20, blank=True)),
                ('mobile_phone', models.CharField(max_length=20, blank=True)),
                ('work_phone', models.CharField(max_length=20, blank=True)),
                ('occupation', models.CharField(max_length=100, blank=True)),
                ('modified_duties_availability', models.NullBooleanField()),
                ('occupational_status', models.CharField(blank=True, max_length=20, choices=[(b'Full-time', b'Full-time'), (b'Part-time', b'Part-time'), (b'Modified Duties', b'Modified Duties'), (b'NotReturned', b'NotReturned'), (b'Unemployed', b'Unemployed'), (b'Retired', b'Retired')])),
                ('job_requirements', models.CharField(blank=True, max_length=20, choices=[(b'Mainly sitting', b'Mainly sitting'), (b'Mainly standing', b'Mainly standing'), (b'Light labour', b'Light labour'), (b'Heavy labour', b'Heavy labour')])),
                ('marital_status', models.CharField(blank=True, max_length=20, choices=[(b'Married', b'Married'), (b'Single', b'Single'), (b'Divorced', b'Divorced'), (b'Common Law', b'Common Law')])),
                ('number_of_children', models.IntegerField(blank=True)),
                ('ages', models.IntegerField(blank=True)),
                ('emergency_contact_name', models.CharField(max_length=100, blank=True)),
                ('emergency_contact_phone', models.CharField(max_length=20, blank=True)),
                ('emergency_contact_relationship', models.CharField(max_length=20, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WomenOnlyChoices',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='healthhistory',
            name='PreviousConditions',
        ),
        migrations.AddField(
            model_name='healthhistory',
            name='cnd_disorders',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='healthhistory',
            name='current_medications',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='healthhistory',
            name='family_doctor',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='healthhistory',
            name='family_doctor_telephone',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='healthhistory',
            name='menstrual_flow',
            field=models.CharField(blank=True, max_length=20, choices=[(b'Reg.', b'Reg.'), (b'Irreg.', b'Irreg.'), (b'Pain/Cramps', b'Pain/Cramps')]),
        ),
        migrations.AddField(
            model_name='healthhistory',
            name='other_conditions',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='healthhistory',
            name='pregnant',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='healthhistory',
            name='previous_conditions',
            field=models.ManyToManyField(to='MedicalForms.PreviousConditions', blank=True),
        ),
        migrations.AddField(
            model_name='healthhistory',
            name='previous_surgeries',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='healthhistory',
            name='smoker',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='healthhistory',
            name='today_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 27, 14, 44, 11, 145190, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='healthhistory',
            name='cardiovascular',
            field=models.ManyToManyField(to='MedicalForms.Cardiovascular', blank=True),
        ),
        migrations.AlterField(
            model_name='healthhistory',
            name='gastrointestinal',
            field=models.ManyToManyField(to='MedicalForms.Gastrointestinal', blank=True),
        ),
        migrations.AlterField(
            model_name='healthhistory',
            name='general',
            field=models.ManyToManyField(to='MedicalForms.General', blank=True),
        ),
        migrations.AlterField(
            model_name='healthhistory',
            name='genitourinary',
            field=models.ManyToManyField(to='MedicalForms.Genitourinary', blank=True),
        ),
        migrations.AlterField(
            model_name='healthhistory',
            name='muscle_joint',
            field=models.ManyToManyField(to='MedicalForms.MuscleJoint', blank=True),
        ),
        migrations.AlterField(
            model_name='healthhistory',
            name='respiratory',
            field=models.ManyToManyField(to='MedicalForms.Respiratory', blank=True),
        ),
        migrations.AlterField(
            model_name='healthhistory',
            name='skin',
            field=models.ManyToManyField(to='MedicalForms.Skin', blank=True),
        ),
        migrations.AddField(
            model_name='accidenthistory',
            name='body_part_collision',
            field=models.ManyToManyField(to='MedicalForms.BodyPart', blank=True),
        ),
        migrations.AddField(
            model_name='accidenthistory',
            name='passengers',
            field=models.ManyToManyField(to='MedicalForms.PassengerLocation'),
        ),
        migrations.AddField(
            model_name='accidenthistory',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='healthhistory',
            name='woemn_only_choices',
            field=models.ManyToManyField(to='MedicalForms.WomenOnlyChoices'),
        ),
    ]
