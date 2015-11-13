# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import MedicalForms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalAppointments', '0007_auto_20151112_1216'),
        ('MedicalForms', '0007_auto_20151113_0051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assessment',
            name='id',
        ),
        migrations.RemoveField(
            model_name='assessment',
            name='user',
        ),
        migrations.AddField(
            model_name='assessment',
            name='patient',
            field=models.OneToOneField(primary_key=True, default=4, serialize=False, to='MedicalAppointments.Patient'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assessment',
            name='assessment',
            field=MedicalForms.utils.MyTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='cardio',
            field=MedicalForms.utils.MyCharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='clinician',
            field=MedicalForms.utils.MyCharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='date',
            field=MedicalForms.utils.MyDateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='education',
            field=MedicalForms.utils.MyTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='heat',
            field=MedicalForms.utils.MyCharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='ice',
            field=MedicalForms.utils.MyCharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='ifc',
            field=MedicalForms.utils.MyCharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='objective',
            field=MedicalForms.utils.MyTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='ohter',
            field=MedicalForms.utils.MyTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='smt',
            field=MedicalForms.utils.MyTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='strength',
            field=MedicalForms.utils.MyCharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='stretch',
            field=MedicalForms.utils.MyCharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='stt',
            field=MedicalForms.utils.MyTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='subjective_choices',
            field=MedicalForms.utils.MySelectField(max_length=15, blank=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='subjective_description',
            field=MedicalForms.utils.MyTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='today_date',
            field=MedicalForms.utils.MyDateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='u_s',
            field=MedicalForms.utils.MyCharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='visit_number',
            field=MedicalForms.utils.MyIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='headachequestions',
            name='aggravated_by_movements',
            field=MedicalForms.utils.MyCharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='headachequestions',
            name='duration',
            field=MedicalForms.utils.MyCharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='headachequestions',
            name='intensity',
            field=MedicalForms.utils.IntegerRangeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='headachequestions',
            name='numbness',
            field=MedicalForms.utils.MyNullBooleanField(),
        ),
        migrations.AlterField(
            model_name='headachequestions',
            name='paraesthesia',
            field=MedicalForms.utils.MyNullBooleanField(),
        ),
        migrations.AlterField(
            model_name='headachequestions',
            name='relieved_by',
            field=MedicalForms.utils.MyNullBooleanField(),
        ),
        migrations.AlterField(
            model_name='headachequestions',
            name='today_date',
            field=MedicalForms.utils.MyDateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='lumbarspinequestions',
            name='aggravated_by_movements',
            field=MedicalForms.utils.MyCharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='lumbarspinequestions',
            name='duration',
            field=MedicalForms.utils.MyCharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='lumbarspinequestions',
            name='intensity',
            field=MedicalForms.utils.IntegerRangeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='lumbarspinequestions',
            name='numbness',
            field=MedicalForms.utils.MyNullBooleanField(),
        ),
        migrations.AlterField(
            model_name='lumbarspinequestions',
            name='paraesthesia',
            field=MedicalForms.utils.MyNullBooleanField(),
        ),
        migrations.AlterField(
            model_name='lumbarspinequestions',
            name='relieved_by',
            field=MedicalForms.utils.MyNullBooleanField(),
        ),
        migrations.AlterField(
            model_name='lumbarspinequestions',
            name='today_date',
            field=MedicalForms.utils.MyDateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='otherquestions',
            name='aggravated_by_movements',
            field=MedicalForms.utils.MyCharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='otherquestions',
            name='duration',
            field=MedicalForms.utils.MyCharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='otherquestions',
            name='intensity',
            field=MedicalForms.utils.IntegerRangeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='otherquestions',
            name='numbness',
            field=MedicalForms.utils.MyNullBooleanField(),
        ),
        migrations.AlterField(
            model_name='otherquestions',
            name='pain_location',
            field=MedicalForms.utils.MyCharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='otherquestions',
            name='paraesthesia',
            field=MedicalForms.utils.MyNullBooleanField(),
        ),
        migrations.AlterField(
            model_name='otherquestions',
            name='radiation',
            field=MedicalForms.utils.MyNullBooleanField(),
        ),
        migrations.AlterField(
            model_name='otherquestions',
            name='relieved_by',
            field=MedicalForms.utils.MyNullBooleanField(),
        ),
        migrations.AlterField(
            model_name='otherquestions',
            name='today_date',
            field=MedicalForms.utils.MyDateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='peripheraljointbasequestions',
            name='aggravated_by_movements',
            field=MedicalForms.utils.MyCharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='peripheraljointbasequestions',
            name='duration',
            field=MedicalForms.utils.MyCharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='peripheraljointbasequestions',
            name='intensity',
            field=MedicalForms.utils.IntegerRangeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='peripheraljointbasequestions',
            name='numbness',
            field=MedicalForms.utils.MyNullBooleanField(),
        ),
        migrations.AlterField(
            model_name='peripheraljointbasequestions',
            name='paraesthesia',
            field=MedicalForms.utils.MyNullBooleanField(),
        ),
        migrations.AlterField(
            model_name='peripheraljointbasequestions',
            name='relieved_by',
            field=MedicalForms.utils.MyNullBooleanField(),
        ),
        migrations.AlterField(
            model_name='peripheraljointbasequestions',
            name='today_date',
            field=MedicalForms.utils.MyDateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='thoracicspinequestions',
            name='aggravated_by_movements',
            field=MedicalForms.utils.MyCharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='thoracicspinequestions',
            name='duration',
            field=MedicalForms.utils.MyCharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='thoracicspinequestions',
            name='intensity',
            field=MedicalForms.utils.IntegerRangeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='thoracicspinequestions',
            name='numbness',
            field=MedicalForms.utils.MyNullBooleanField(),
        ),
        migrations.AlterField(
            model_name='thoracicspinequestions',
            name='paraesthesia',
            field=MedicalForms.utils.MyNullBooleanField(),
        ),
        migrations.AlterField(
            model_name='thoracicspinequestions',
            name='relieved_by',
            field=MedicalForms.utils.MyNullBooleanField(),
        ),
        migrations.AlterField(
            model_name='thoracicspinequestions',
            name='today_date',
            field=MedicalForms.utils.MyDateTimeField(auto_now_add=True, null=True),
        ),
    ]
