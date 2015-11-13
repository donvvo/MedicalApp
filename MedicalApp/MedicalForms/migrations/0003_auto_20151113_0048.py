# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import MedicalForms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalAppointments', '0007_auto_20151112_1216'),
        ('MedicalForms', '0002_auto_20151112_2051'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcuteConcussionEvaluation',
            fields=[
                ('patient', models.OneToOneField(primary_key=True, serialize=False, to='MedicalAppointments.Patient')),
                ('dob', MedicalForms.utils.MyDateTimeField(null=True, blank=True)),
                ('date_of_injury', MedicalForms.utils.MyDateTimeField(null=True, blank=True)),
                ('reporter', MedicalForms.utils.MySelectField(max_length=10, blank=True)),
                ('injury_description', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('evidence_of_blow', MedicalForms.utils.MyNullBooleanField()),
                ('evidence_of_cranial_injury', MedicalForms.utils.MyNullBooleanField()),
                ('cause', MedicalForms.utils.MySelectField(max_length=20, blank=True)),
                ('sports_specify', MedicalForms.utils.MyCharField(max_length=50, blank=True)),
                ('others_specify', MedicalForms.utils.MyCharField(max_length=50, blank=True)),
                ('amnesia_before', MedicalForms.utils.MyNullBooleanField()),
                ('amnesia_before_duration', MedicalForms.utils.MyCharField(max_length=10, blank=True)),
                ('amnesia_after', MedicalForms.utils.MyNullBooleanField()),
                ('amnesia_after_duration', MedicalForms.utils.MyCharField(max_length=10, blank=True)),
                ('lost_of_consciousness', MedicalForms.utils.MyNullBooleanField()),
                ('lost_of_consciousness_duration', MedicalForms.utils.MyCharField(max_length=10, blank=True)),
                ('seizure', MedicalForms.utils.MyNullBooleanField()),
                ('seizure_detail', MedicalForms.utils.MyCharField(max_length=10, blank=True)),
                ('headache', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('nausea', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('vomiting', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('balance_problems', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('dizziness', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('visual_problems', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('fatigue', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('sensitivity_to_light', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('sensitivity_to_noise', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('numbness_and_tingling', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('physical_total', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('foggy', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('slow_down', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('difficulty_concentrating', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('difficulty_remembering', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('cognitive_total', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('irritability', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('sadness', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('more_emotional', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('nervousness', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('emotional_total', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('drowsiness', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('sleeping_less', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('sleeping_more', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('trouble_falling_asleep', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('sleep_total', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('all_total', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('excertion_physical', MedicalForms.utils.MyNullBooleanField()),
                ('excertion_cognitive', MedicalForms.utils.MyNullBooleanField()),
                ('overall_rating', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('concussion_history', MedicalForms.utils.MyNullBooleanField()),
                ('previous_number', MedicalForms.utils.IntegerRangeField(null=True, blank=True)),
                ('longest_duration', MedicalForms.utils.MySelectField(max_length=10, blank=True)),
                ('less_force_caused_reinjury', MedicalForms.utils.MyNullBooleanField()),
                ('headache_history', MedicalForms.utils.MyNullBooleanField()),
                ('prior_treatment', MedicalForms.utils.MyNullBooleanField()),
                ('history_of_migraine', MedicalForms.utils.MyNullBooleanField()),
                ('personal_family', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('learning_disabilities', MedicalForms.utils.MyNullBooleanField()),
                ('attention_deficit', MedicalForms.utils.MyNullBooleanField()),
                ('other_developmental', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('anxiety', MedicalForms.utils.MyNullBooleanField()),
                ('depression', MedicalForms.utils.MyNullBooleanField()),
                ('sleep_disorder', MedicalForms.utils.MyNullBooleanField()),
                ('other_psychiatric', MedicalForms.utils.MyCharField(max_length=100, blank=True)),
                ('list_other_disorders', MedicalForms.utils.MyCharField(max_length=200, blank=True)),
                ('follow_up', MedicalForms.utils.MySelectField(max_length=30, blank=True)),
                ('refferal_others', MedicalForms.utils.MyCharField(max_length=50, blank=True)),
                ('completed_date', MedicalForms.utils.MyDateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='EarlySign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='LocationImpact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='RedFlags',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Refferal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='tmjscreening',
            name='pain',
            field=models.ManyToManyField(to='MedicalForms.Pain'),
        ),
        migrations.AlterField(
            model_name='tmjscreening',
            name='symptom',
            field=models.ManyToManyField(to='MedicalForms.Symptom'),
        ),
        migrations.AddField(
            model_name='acuteconcussionevaluation',
            name='dignosis',
            field=models.ManyToManyField(to='MedicalForms.Diagnosis', blank=True),
        ),
        migrations.AddField(
            model_name='acuteconcussionevaluation',
            name='doctor',
            field=models.ForeignKey(blank=True, to='MedicalAppointments.Doctor', null=True),
        ),
        migrations.AddField(
            model_name='acuteconcussionevaluation',
            name='early_signs',
            field=models.ManyToManyField(to='MedicalForms.EarlySign', blank=True),
        ),
        migrations.AddField(
            model_name='acuteconcussionevaluation',
            name='location_of_impact',
            field=models.ManyToManyField(to='MedicalForms.LocationImpact', blank=True),
        ),
        migrations.AddField(
            model_name='acuteconcussionevaluation',
            name='red_flags',
            field=models.ManyToManyField(to='MedicalForms.RedFlags', blank=True),
        ),
        migrations.AddField(
            model_name='acuteconcussionevaluation',
            name='refferal',
            field=models.ManyToManyField(to='MedicalForms.Refferal', blank=True),
        ),
    ]
