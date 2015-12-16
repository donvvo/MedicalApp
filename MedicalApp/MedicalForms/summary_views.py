from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import redirect
from django.views.generic import TemplateView

from braces.views import LoginRequiredMixin, StaffuserRequiredMixin

from MedicalAppointments.models import Clinic, Patient
from .models import LowerExtremity


class LowerExtremitySummaryView(LoginRequiredMixin, StaffuserRequiredMixin, TemplateView):
    template_name = 'medicalforms/table_summary/lower_extremity_summary.html'
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super(LowerExtremitySummaryView, self).get_context_data(**kwargs)
        context['summary'] = LowerExtremity.objects.table_summary()
        context['clinics_num'] = Clinic.objects.all().count()
        context['patients_num'] = Patient.objects.all().count()

        print context['summary']

        return context