from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import UpdateView, TemplateView, CreateView
from django.utils.decorators import method_decorator

from braces.views import LoginRequiredMixin, GroupRequiredMixin

from MedicalApp.utils import user_passes_test_with_kwargs
from MedicalApp.users.models import User
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
        return reverse_lazy('users:patient_profile', kwargs={'user_id': self.user_id})


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


class PatientSpecificView(DoctorFormBaseView):
    template_name = 'medicalforms/doctor_forms/patient_specific_functional_scale.html'
    model = PatientSpecific
    form_class = PatientSpecificForm


class AttendanceSheetView(DoctorOnlyMixin, TemplateView):
    template_name = 'medicalforms/doctor_forms/attendance_sheet.html'

    def get_context_data(self, **kwargs):
        context = super(AttendanceSheetView, self).get_context_data(**kwargs)

        self.user_id = self.kwargs['user_id']
        context['user'] = get_object_or_404(User, pk=self.user_id)
        context['treatment_plan'] = TreatmentPlan.objects.filter(patient_id=self.user_id).all()
        context['date_signature'] = DateSignature.objects.filter(patient_id=self.user_id).all()

        return context


class TreatmentPlanAddView(DoctorFormBaseView):
    template_name = 'medicalforms/doctor_forms/treatmentplan_add.html'
    model = TreatmentPlan
    form_class = TreatmentPlanAddForm

    def get_object(self):
        self.user_id = self.kwargs['user_id']
        return self.model(patient_id=self.user_id)

    def get_success_url(self):
        return reverse_lazy('medical_forms:attendance-sheet', kwargs={'user_id': self.user_id})


class DateSignatureAddView(DoctorFormBaseView):
    template_name = 'medicalforms/doctor_forms/datesignature_add.html'
    model = DateSignature
    form_class = DateSignatureAddForm

    def get_object(self):
        self.user_id = self.kwargs['user_id']
        return self.model(patient_id=self.user_id)

    def get_success_url(self):
        return reverse_lazy('medical_forms:attendance-sheet', kwargs={'user_id': self.user_id})
