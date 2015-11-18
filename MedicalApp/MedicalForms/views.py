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
from .patient_form_views import ChiropracticTreatmentView, PhysiotherapyTreatmentView,\
    MassageTreatmentView, MedicalAuthorizationView, ExchangeInformationView
from .models import *
from .forms import *


def owner_or_doctors(user, **kwargs):
    user_id = int(kwargs['user_id'])
    return user.pk == user_id or user.groups.filter(name="Doctors").exists()


class DoctorOnlyMixin(LoginRequiredMixin, GroupRequiredMixin):
    group_required = 'Doctors'
    raise_exception = True


class PatientFormBaseView(LoginRequiredMixin, UpdateView):
    # Only allows access to doctors or patients to their own forms
    @method_decorator(user_passes_test_with_kwargs(owner_or_doctors))
    def dispatch(self, request, *args, **kwargs):
        self.user_id = int(kwargs['user_id'])
        return super(PatientFormBaseView, self). dispatch(request, *args, **kwargs)

    def get_object(self):
        objects = self.model.objects.filter(pk=self.user_id)
        if objects.exists():
            return objects.get()
        else:
            return self.model(pk=self.user_id)


class DoctorFormBaseView(DoctorOnlyMixin, UpdateView):
    def get_object(self):
        self.user_id = self.kwargs['user_id']
        objects = self.model.objects.filter(pk=self.user_id)
        if objects.exists():
            return objects.get()
        else:
            return self.model(pk=self.user_id)


class PatientInformationView(PatientFormBaseView):
    template_name = 'medicalforms/patient_information.html'
    model = PatientInformation
    form_class = PatientInformationForm

    def get_success_url(self):
        return reverse_lazy('medical_forms:patient_info', kwargs={'user_id': self.user_id})


class HealthHistoryView(PatientFormBaseView):
    template_name = 'medicalforms/health_history.html'
    model = HealthHistory
    form_class = HealthHistoryForm

    def get_success_url(self):
        return reverse_lazy('medical_forms:health_history', kwargs={'user_id': self.user_id})


class AccidentHistoryView(PatientFormBaseView):
    template_name = 'medicalforms/accident_history.html'
    model = AccidentHistory
    form_class = AccidentHistoryForm

    def get_success_url(self):
        return reverse_lazy('medical_forms:accident-history', kwargs={'user_id': self.user_id})


class TMJScreeningView(PatientFormBaseView):
    template_name = 'medicalforms/tmj_screening.html'
    model = TMJScreening
    form_class = TMJScreeningForm

    def get_success_url(self):
        return reverse_lazy('medical_forms:tmj-screening', kwargs={'user_id': self.user_id})


class AssessmentView(DoctorFormBaseView):
    template_name = 'medicalforms/assessment.html'
    model = Assessment
    form_class = AssessmentForm

    def get_success_url(self):
        return reverse_lazy('medical_forms:assessment', kwargs={'user_id': self.user_id})


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


class AcuteConcussionEvaluationView(DoctorFormBaseView):
    template_name = 'medicalforms/accute_concussion_eval.html'
    model = AcuteConcussionEvaluation
    form_class = AcuteConcussionEvaluationForm

    def get_success_url(self):
        return reverse_lazy('medical_forms:acute-concussion-eval', kwargs={'user_id': self.user_id})


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
