from django.core.urlresolvers import reverse_lazy
from django.views.generic import UpdateView
from django.utils.decorators import method_decorator

from braces.views import LoginRequiredMixin

from MedicalApp.utils import user_passes_test_with_kwargs
from .models import *
from .forms import *


def owner_or_doctors(user, **kwargs):
    user_id = int(kwargs['user_id'])
    return user.pk == user_id or user.groups.filter(name="Doctors").exists()


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

    def get_success_url(self):
        return reverse_lazy('users:patient_profile', kwargs={'username': self.object.patient.user.username})


# Patient forms
class PatientInformationView(PatientFormBaseView):
    template_name = 'medicalforms/patient_forms/patient_information.html'
    model = PatientInformation
    form_class = PatientInformationForm


class HealthHistoryView(PatientFormBaseView):
    template_name = 'medicalforms/patient_forms/health_history.html'
    model = HealthHistory
    form_class = HealthHistoryForm


class AccidentHistoryView(PatientFormBaseView):
    template_name = 'medicalforms/patient_forms/accident_history.html'
    model = AccidentHistory
    form_class = AccidentHistoryForm


# Consent form views.
class ChiropracticTreatmentView(PatientFormBaseView):
    template_name = 'medicalforms/consent_forms/chiropractic_consent.html'
    model = ChiropracticTreatment
    form_class = ChiropracticTreatmentForm


class PhysiotherapyTreatmentView(PatientFormBaseView):
    template_name = 'medicalforms/consent_forms/physiotherapy_consent.html'
    model = PhysiotherapyTreatment
    form_class = PhysiotherapyTreatmentForm


class MassageTreatmentView(PatientFormBaseView):
    template_name = 'medicalforms/consent_forms/massage_consent.html'
    model = MassageTreatment
    form_class = MassageTreatmentForm


class MedicalAuthorizationView(PatientFormBaseView):
    template_name = 'medicalforms/consent_forms/medical_authorization.html'
    model = MedicalAuthorization
    form_class = MedicalAuthorizationForm


class ExchangeInformationView(PatientFormBaseView):
    template_name = 'medicalforms/consent_forms/exchange_of_medical_info.html'
    model = ExchangeInformation
    form_class = ExchangeInformationForm


class AuthorizationAndDirectionView(PatientFormBaseView):
    template_name = 'medicalforms/consent_forms/authorization_and_direction.html'
    model = AuthorizationAndDirection
    form_class = AuthorizationAndDirectionForm


class Section47View(PatientFormBaseView):
    template_name = 'medicalforms/consent_forms/section_47.html'
    model = Section47
    form_class = Section47Form


class StatutoryAccidentsBenefitsView(PatientFormBaseView):
    template_name = 'medicalforms/consent_forms/statutory_accidents_benefits.html'
    model = StatutoryAccidentsBenefits
    form_class = StatutoryAccidentsBenefitsForm
