from django.core.urlresolvers import reverse_lazy
from django.views.generic import UpdateView
from django.utils.decorators import method_decorator

from braces.views import LoginRequiredMixin, GroupRequiredMixin

from MedicalApp.utils import user_passes_test_with_kwargs
from .models import *
from .forms import *


class DoctorOnlyMixin(LoginRequiredMixin, GroupRequiredMixin):
    group_required = 'Doctors'
    raise_exception = True


class DoctorFormBaseView(DoctorOnlyMixin, UpdateView):
    def get_object(self):
        self.user_id = self.kwargs['user_id']
        objects = self.model.objects.filter(pk=self.user_id)
        if objects.exists():
            return objects.get()
        else:
            return self.model(pk=self.user_id)

    def get_success_url(self):
        return reverse_lazy('users:patient_profile', kwargs={'username': self.object.patient.user.username})


# Doctor forms
class PlanOfManagementView(DoctorFormBaseView):
    template_name = 'medicalforms/doctor_forms/plan_of_management.html'
    model = PlanOfManagement
    form_class = PlanOfManagementForm


class PatientDischargeView(DoctorFormBaseView):
    template_name = 'medicalforms/doctor_forms/patient_discharge.html'
    model = PatientDischarge
    form_class = PatientDischargeForm


class ReportOfFindingsView(DoctorFormBaseView):
    template_name = 'medicalforms/doctor_forms/report_of_findings.html'
    model = ReportOfFindings
    form_class = ReportOfFindingsForm

