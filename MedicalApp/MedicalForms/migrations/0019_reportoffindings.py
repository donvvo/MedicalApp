# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import MedicalForms.utils


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalAppointments', '0006_auto_20151111_0015'),
        ('MedicalForms', '0018_auto_20151107_1615'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportOfFindings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_of_assessment', models.DateTimeField(blank=True)),
                ('presenting_complaint', MedicalForms.utils.MyTextField(blank=True)),
                ('examination_findings', MedicalForms.utils.MyTextField(blank=True)),
                ('diagnosis', MedicalForms.utils.MyTextField(blank=True)),
                ('plan_of_management', MedicalForms.utils.MyTextField(blank=True)),
                ('goals', MedicalForms.utils.MyTextField(blank=True)),
                ('risks_discussed', MedicalForms.utils.MyTextField(blank=True)),
                ('alternatives', MedicalForms.utils.MyTextField(blank=True)),
                ('prognosis', MedicalForms.utils.MyTextField(blank=True)),
                ('estimated_time_for_recovery', MedicalForms.utils.MyCharField(max_length=20, blank=True)),
                ('patient_questions', MedicalForms.utils.MyTextField(blank=True)),
                ('doctor', models.ForeignKey(to='MedicalAppointments.Doctor')),
                ('patient', models.ForeignKey(to='MedicalAppointments.Patient')),
            ],
        ),
    ]
