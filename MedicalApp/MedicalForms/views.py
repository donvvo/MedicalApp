# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import FormView
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import FormMixin, ProcessFormView

from braces.views import LoginRequiredMixin

from .models import PatientInformation, HealthHistory
from .forms import PatientInformationForm, HealthHistoryForm,\
    HeadacheQuestionForm, CervicalSpineQuestionForm, ThoracicSpineQuestionForm,\
    LumbarSpineQuestionForm, PeripheralJointQuestion1Form,\
    PeripheralJointQuestion2Form, PeripheralJointQuestion3Form,\
    PeripheralJointQuestion4Form, OtherSubjectiveEvaluationQuestionForm,\
    AssessmentForm, AccidentHistoryForm


class PatientInformationView(FormView):
    template_name = 'medicalforms/patient_information.html'
    form_class = PatientInformationForm


class HealthHistoryView(FormView):
    template_name = 'medicalforms/health_history.html'
    form_class = HealthHistoryForm


class AssessmentView(FormView):
    template_name = 'medicalforms/assessment.html'
    form_class = AssessmentForm


class AccidentHistoryView(FormView):
    template_name = 'medicalforms/accident_history.html'
    form_class = AccidentHistoryForm


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
