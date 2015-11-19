# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import MedicalForms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalForms', '0021_auto_20151119_0116'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArmsLeftRight',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='EmergencyPersonnel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Examinations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='LegsLeftRight',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ShouldersLeftRight',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='accidenthistory',
            name='arms',
            field=MedicalForms.utils.MySelectField(max_length=10, blank=True),
        ),
        migrations.AddField(
            model_name='accidenthistory',
            name='back',
            field=MedicalForms.utils.MySelectField(max_length=10, blank=True),
        ),
        migrations.AddField(
            model_name='accidenthistory',
            name='bleeding',
            field=MedicalForms.utils.MyCharField(max_length=30, blank=True),
        ),
        migrations.AddField(
            model_name='accidenthistory',
            name='chest_pain',
            field=MedicalForms.utils.MySelectField(max_length=10, blank=True),
        ),
        migrations.AddField(
            model_name='accidenthistory',
            name='dizziness',
            field=MedicalForms.utils.MySelectField(max_length=10, blank=True),
        ),
        migrations.AddField(
            model_name='accidenthistory',
            name='doctor_date',
            field=MedicalForms.utils.MyDateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='accidenthistory',
            name='doctor_name',
            field=MedicalForms.utils.MyCharField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='accidenthistory',
            name='examination_date',
            field=MedicalForms.utils.MyDateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='accidenthistory',
            name='examination_other',
            field=MedicalForms.utils.MyCharField(max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='accidenthistory',
            name='head_neck',
            field=MedicalForms.utils.MySelectField(max_length=10, blank=True),
        ),
        migrations.AddField(
            model_name='accidenthistory',
            name='headache',
            field=MedicalForms.utils.MySelectField(max_length=10, blank=True),
        ),
        migrations.AddField(
            model_name='accidenthistory',
            name='hospitalized',
            field=MedicalForms.utils.MyNullBooleanField(),
        ),
        migrations.AddField(
            model_name='accidenthistory',
            name='legs',
            field=MedicalForms.utils.MySelectField(max_length=10, blank=True),
        ),
        migrations.AddField(
            model_name='accidenthistory',
            name='nausea_voimit',
            field=MedicalForms.utils.MySelectField(max_length=10, blank=True),
        ),
        migrations.AddField(
            model_name='accidenthistory',
            name='other',
            field=MedicalForms.utils.MyCharField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='accidenthistory',
            name='seen_doctor',
            field=MedicalForms.utils.MyNullBooleanField(),
        ),
        migrations.AddField(
            model_name='accidenthistory',
            name='shoulders',
            field=MedicalForms.utils.MySelectField(max_length=10, blank=True),
        ),
        migrations.AddField(
            model_name='accidenthistory',
            name='transportation',
            field=MedicalForms.utils.MySelectField(max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='accidenthistory',
            name='treatment',
            field=MedicalForms.utils.MyCharField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='accidenthistory',
            name='treatment_recommendation',
            field=MedicalForms.utils.MyCharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='accidenthistory',
            name='arms_which',
            field=models.ManyToManyField(to='MedicalForms.ArmsLeftRight', blank=True),
        ),
        migrations.AddField(
            model_name='accidenthistory',
            name='emergency_personnel',
            field=models.ManyToManyField(to='MedicalForms.EmergencyPersonnel', blank=True),
        ),
        migrations.AddField(
            model_name='accidenthistory',
            name='examination_type',
            field=models.ManyToManyField(to='MedicalForms.Examinations', blank=True),
        ),
        migrations.AddField(
            model_name='accidenthistory',
            name='legs_which',
            field=models.ManyToManyField(to='MedicalForms.LegsLeftRight', blank=True),
        ),
        migrations.AddField(
            model_name='accidenthistory',
            name='shoulders_which',
            field=models.ManyToManyField(to='MedicalForms.ShouldersLeftRight', blank=True),
        ),
    ]
