# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib.auth.decorators import user_passes_test
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseForbidden
from django.views.generic import FormView, DetailView, ListView, CreateView, UpdateView
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import FormMixin, ProcessFormView
from django.shortcuts import get_object_or_404, redirect
from django.utils.decorators import method_decorator

from braces.views import LoginRequiredMixin, GroupRequiredMixin

from MedicalApp.utils import user_passes_test_with_kwargs
from .models import *
from .forms import *


def owner_or_doctors(user, **kwargs):
    user_id = int(kwargs['user_id'])
    return user.pk == user_id or user.groups.filter(name="Doctors").exists()


class DoctorOnlyMixin(LoginRequiredMixin, GroupRequiredMixin):
    group_required = 'Doctors'
    raise_exception = True


# Patient information
class PatientInformationView(LoginRequiredMixin, DetailView):
    template_name = 'medicalforms/patient_information.html'
    model = PatientInformation

    @method_decorator(user_passes_test_with_kwargs(owner_or_doctors))
    def dispatch(self, request, *args, **kwargs):
        user_id = int(kwargs['user_id'])
        self.patient_info_form = self.model.objects.filter(pk=user_id)
        if self.patient_info_form.exists():
            return super(PatientInformationView, self).dispatch(request, *args, **kwargs)
        else:
            return redirect(reverse_lazy('medical_forms:patient_info_edit',
                            kwargs={'user_id': user_id}))

    def get_object(self):
        return self.patient_info_form.get()


class PatientInformationEditView(LoginRequiredMixin, UpdateView):
    template_name = 'medicalforms/patient_information_edit.html'
    model = PatientInformation
    form_class = PatientInformationForm

    @method_decorator(user_passes_test_with_kwargs(owner_or_doctors))
    def dispatch(self, request, *args, **kwargs):
        self.user_id = int(kwargs['user_id'])
        return super(PatientInformationEditView, self). dispatch(request, *args, **kwargs)

    def get_object(self):
        objects = self.model.objects.filter(pk=self.user_id)
        if objects.exists():
            return objects.get()
        else:
            return PatientInformation(pk=self.user_id)

    def get_success_url(self):
        return reverse_lazy('medical_forms:patient_info', kwargs={'user_id': self.user_id})


class PatientInformationCreateView(LoginRequiredMixin, CreateView):
    template_name = 'medicalforms/patient_information_edit.html'
    model = PatientInformation
    form_class = PatientInformationForm
    success_url = reverse_lazy('medical_forms:patient_info_new')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ReportOfFindingsCreateView, self).form_valid(form)


class HealthHistoryView(FormView):
    template_name = 'medicalforms/health_history.html'
    form_class = HealthHistoryForm


class AssessmentView(FormView):
    template_name = 'medicalforms/assessment.html'
    form_class = AssessmentForm


class AccidentHistoryView(FormView):
    template_name = 'medicalforms/accident_history.html'
    form_class = AccidentHistoryForm


class MVAIntakeView(FormView):
    template_name = 'medicalforms/MVA_intake.html'
    form_class = MVAIntakeForm


# Report of findings
class ReportOfFindingsView(DoctorOnlyMixin, DetailView):
    template_name = 'medicalforms/report_of_findings.html'
    model = ReportOfFindings
    # These next two lines tell the view to index lookups by username
    slug_field = "pk"
    slug_url_kwarg = "pk"


class ReportOfFindingsListView(DoctorOnlyMixin, ListView):
    template_name = 'medicalforms/report_of_findings_list.html'
    model = ReportOfFindings

    def get_queryset(self):
        return self.model.objects.filter(doctor=self.request.user.doctor).all()


class ReportOfFindingsEditView(DoctorOnlyMixin, UpdateView):
    template_name = 'medicalforms/report_of_findings_edit.html'
    model = ReportOfFindings
    form_class = ReportOffindingsForm
    success_url = reverse_lazy('medical_forms:report_of_findings_list')
    slug_field = "pk"
    slug_url_kwarg = "pk"


class ReportOfFindingsCreateView(DoctorOnlyMixin, CreateView):
    template_name = 'medicalforms/report_of_findings_edit.html'
    model = ReportOfFindings
    form_class = ReportOffindingsForm
    success_url = reverse_lazy('medical_forms:report_of_findings_new')

    def form_valid(self, form):
        form.instance.doctor = self.request.user.doctor
        return super(ReportOfFindingsCreateView, self).form_valid(form)


# From https://gist.github.com/michelts/1029336#file-gistfile1-py-L6
class MultipleFormsMixin(FormMixin):
    """
    A mixin that provides a way to show and handle several forms in a
    request.
    """
    form_classes = {} # set the form classes as a mapping

    def get_form_classes(self):
        return self.form_classes

    def get_forms(self, form_classes):
        return dict([(key, klass(**self.get_form_kwargs())) \
            for key, klass in form_classes.items()])

    def forms_valid(self, forms):
        return super(MultipleFormsMixin, self).form_valid(forms)

    def forms_invalid(self, forms):
        return self.render_to_response(self.get_context_data(forms=forms))


class ProcessMultipleFormsView(ProcessFormView):
    """
    A mixin that processes multiple forms on POST. Every form must be
    valid.
    """
    def get(self, request, *args, **kwargs):
        form_classes = self.get_form_classes()
        forms = self.get_forms(form_classes)
        return self.render_to_response(self.get_context_data(forms=forms))

    def post(self, request, *args, **kwargs):
        form_classes = self.get_form_classes()
        forms = self.get_forms(form_classes)
        if all([form.is_valid() for form in forms.values()]):
            return self.forms_valid(forms)
        else:
            return self.forms_invalid(forms)


class BaseMultipleFormsView(MultipleFormsMixin, ProcessMultipleFormsView):
    """
    A base view for displaying several forms.
    """


class MultipleFormsView(TemplateResponseMixin, BaseMultipleFormsView):
    """
    A view for displaing several forms, and rendering a template response.
    """


class SubjectiveEvaluationView(MultipleFormsView):
    template_name = 'medicalforms/subjective_evaluation.html'
    form_classes = {
        'headache': HeadacheQuestionForm,
        'cervical': CervicalSpineQuestionForm,
        'thoracic': ThoracicSpineQuestionForm,
        'lumbar': LumbarSpineQuestionForm,
        'joint1': PeripheralJointQuestion1Form,
        'joint2': PeripheralJointQuestion2Form,
        'joint3': PeripheralJointQuestion3Form,
        'joint4': PeripheralJointQuestion4Form,
        'others': OtherSubjectiveEvaluationQuestionForm
    }
