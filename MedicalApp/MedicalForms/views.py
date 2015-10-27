# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import FormView

from braces.views import LoginRequiredMixin

from .models import PatientInformation
from .forms import PatientInformationForm


class PatientInformationView(FormView):
    template_name = 'medicalforms/patient_information.html'
    form_class = PatientInformationForm
