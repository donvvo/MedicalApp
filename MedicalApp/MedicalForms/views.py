# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import FormView

from braces.views import LoginRequiredMixin

from .models import PatientInformation, HealthHistory
from .forms import PatientInformationForm, HealthHistoryForm


class PatientInformationView(FormView):
    template_name = 'medicalforms/patient_information.html'
    form_class = PatientInformationForm


class HealthHistoryView(FormView):
    template_name = 'medicalforms/health_history.html'
    form_class = HealthHistoryForm
