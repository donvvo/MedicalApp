# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MedicalForms', '0006_auto_20151027_0944'),
    ]

    operations = [
        migrations.CreateModel(
            name='AggravatedByHeadache',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AggravatedByOthers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AggravatedByPeripheralJoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='HeadacheQuestions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('today_date', models.DateTimeField(auto_now_add=True)),
                ('intensity', models.IntegerField(blank=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
                ('duration', models.CharField(max_length=20, blank=True)),
                ('numbness', models.NullBooleanField()),
                ('paraesthesia', models.NullBooleanField()),
                ('aggravated_by_movements', models.CharField(max_length=100)),
                ('relieved_by', models.NullBooleanField()),
                ('aggravated_by', models.ManyToManyField(to='MedicalForms.AggravatedByHeadache', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LumbarSpineQuestions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('today_date', models.DateTimeField(auto_now_add=True)),
                ('intensity', models.IntegerField(blank=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
                ('duration', models.CharField(max_length=20, blank=True)),
                ('numbness', models.NullBooleanField()),
                ('paraesthesia', models.NullBooleanField()),
                ('aggravated_by_movements', models.CharField(max_length=100)),
                ('relieved_by', models.NullBooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OtherConditions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='OtherQuestions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('today_date', models.DateTimeField(auto_now_add=True)),
                ('intensity', models.IntegerField(blank=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
                ('duration', models.CharField(max_length=20, blank=True)),
                ('numbness', models.NullBooleanField()),
                ('paraesthesia', models.NullBooleanField()),
                ('aggravated_by_movements', models.CharField(max_length=100)),
                ('relieved_by', models.NullBooleanField()),
                ('radiation', models.NullBooleanField()),
                ('pain_location', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OtherSubjectiveEvaluationQuestions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('today_date', models.DateTimeField(auto_now_add=True)),
                ('conditions', models.ManyToManyField(to='MedicalForms.OtherConditions', blank=True)),
                ('users', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PeripheralJointBaseQuestions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('today_date', models.DateTimeField(auto_now_add=True)),
                ('intensity', models.IntegerField(blank=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
                ('duration', models.CharField(max_length=20, blank=True)),
                ('numbness', models.NullBooleanField()),
                ('paraesthesia', models.NullBooleanField()),
                ('aggravated_by_movements', models.CharField(max_length=100)),
                ('relieved_by', models.NullBooleanField()),
                ('radiation', models.NullBooleanField()),
                ('pain_location', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PresentPain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ThoracicSpineQuestions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('today_date', models.DateTimeField(auto_now_add=True)),
                ('intensity', models.IntegerField(blank=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
                ('duration', models.CharField(max_length=20, blank=True)),
                ('numbness', models.NullBooleanField()),
                ('paraesthesia', models.NullBooleanField()),
                ('aggravated_by_movements', models.CharField(max_length=100)),
                ('relieved_by', models.NullBooleanField()),
                ('present_pain', models.ManyToManyField(to='MedicalForms.PresentPain', blank=True)),
                ('users', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TypeOfPainHeadache',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfPainOthers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='healthhistory',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True),
        ),
        migrations.CreateModel(
            name='CervicalSpineQuestions',
            fields=[
                ('otherquestions_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='MedicalForms.OtherQuestions')),
            ],
            options={
                'abstract': False,
            },
            bases=('MedicalForms.otherquestions',),
        ),
        migrations.CreateModel(
            name='PeripheralJointQuestions1',
            fields=[
                ('peripheraljointbasequestions_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='MedicalForms.PeripheralJointBaseQuestions')),
            ],
            options={
                'abstract': False,
            },
            bases=('MedicalForms.peripheraljointbasequestions',),
        ),
        migrations.CreateModel(
            name='PeripheralJointQuestions2',
            fields=[
                ('peripheraljointbasequestions_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='MedicalForms.PeripheralJointBaseQuestions')),
            ],
            options={
                'abstract': False,
            },
            bases=('MedicalForms.peripheraljointbasequestions',),
        ),
        migrations.CreateModel(
            name='PeripheralJointQuestions3',
            fields=[
                ('peripheraljointbasequestions_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='MedicalForms.PeripheralJointBaseQuestions')),
            ],
            options={
                'abstract': False,
            },
            bases=('MedicalForms.peripheraljointbasequestions',),
        ),
        migrations.CreateModel(
            name='PeripheralJointQuestions4',
            fields=[
                ('peripheraljointbasequestions_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='MedicalForms.PeripheralJointBaseQuestions')),
            ],
            options={
                'abstract': False,
            },
            bases=('MedicalForms.peripheraljointbasequestions',),
        ),
        migrations.AddField(
            model_name='peripheraljointbasequestions',
            name='aggravated_by',
            field=models.ManyToManyField(to='MedicalForms.AggravatedByPeripheralJoint', blank=True),
        ),
        migrations.AddField(
            model_name='peripheraljointbasequestions',
            name='present_pain',
            field=models.ManyToManyField(to='MedicalForms.PresentPain', blank=True),
        ),
        migrations.AddField(
            model_name='peripheraljointbasequestions',
            name='type_of_pain',
            field=models.ManyToManyField(to='MedicalForms.TypeOfPainOthers', blank=True),
        ),
        migrations.AddField(
            model_name='peripheraljointbasequestions',
            name='users',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True),
        ),
        migrations.AddField(
            model_name='otherquestions',
            name='aggravated_by',
            field=models.ManyToManyField(to='MedicalForms.AggravatedByOthers', blank=True),
        ),
        migrations.AddField(
            model_name='otherquestions',
            name='present_pain',
            field=models.ManyToManyField(to='MedicalForms.PresentPain', blank=True),
        ),
        migrations.AddField(
            model_name='otherquestions',
            name='type_of_pain',
            field=models.ManyToManyField(to='MedicalForms.TypeOfPainOthers', blank=True),
        ),
        migrations.AddField(
            model_name='otherquestions',
            name='users',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True),
        ),
        migrations.AddField(
            model_name='lumbarspinequestions',
            name='present_pain',
            field=models.ManyToManyField(to='MedicalForms.PresentPain', blank=True),
        ),
        migrations.AddField(
            model_name='lumbarspinequestions',
            name='users',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True),
        ),
        migrations.AddField(
            model_name='headachequestions',
            name='present_pain',
            field=models.ManyToManyField(to='MedicalForms.PresentPain', blank=True),
        ),
        migrations.AddField(
            model_name='headachequestions',
            name='type_of_pain',
            field=models.ManyToManyField(to='MedicalForms.TypeOfPainHeadache', blank=True),
        ),
        migrations.AddField(
            model_name='headachequestions',
            name='users',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
