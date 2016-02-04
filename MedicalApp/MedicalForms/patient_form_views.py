from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import UpdateView
from django.utils.decorators import method_decorator

from braces.views import LoginRequiredMixin

from MedicalApp.utils import user_passes_test_with_kwargs
from .models import *
from .forms import *
from MedicalAppointments.models import Booking
from Notifications.models import Notification


def owner_or_doctors(user, **kwargs):
    user_id = int(kwargs['user_id'])
    return user.pk == user_id or user.groups.filter(name="Doctors").exists() or user.is_staff or \
    user.groups.filter(name="Clinics").exists()


class PatientFormBaseView(LoginRequiredMixin, UpdateView):
    # Only allows access to doctors or patients to their own forms
    @method_decorator(user_passes_test_with_kwargs(owner_or_doctors))
    def dispatch(self, request, *args, **kwargs):
        self.user_id = int(kwargs['user_id'])
        return super(PatientFormBaseView, self). dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        response = super(PatientFormBaseView, self).get(request, *args, **kwargs)
        if self.assigned:
            return response
        else:
            # Only doctors or staff can assign forms
            if request.user.groups.filter(name="Doctors").exists() or request.user.is_staff or \
            request.user.groups.filter(name="Clinics").exists():
                self.initial_form.save()

                # Send notification to patient
                action_type = 'Assign patient form'

                patient_user = get_object_or_404(User, pk=self.user_id)
                subject = self.request.user
                action = 'assigned ' + str(self.initial_form)
                notification = Notification(
                    subject=subject,
                    action_type=action_type,
                    action=action,
                    target=patient_user
                )
                notification.save()

                return redirect(reverse('users:patient_profile', kwargs={'user_id': self.user_id}))
            else:
                raise PermissionDenied

    def get_object(self):
        objects = self.model.objects.filter(pk=self.user_id)
        if objects.exists():
            self.assigned = True
            return objects.get()
        else:
            self.assigned = False
            self.initial_form = self.model(pk=self.user_id)
            return self.initial_form

    def get_success_url(self):
        return reverse_lazy('users:patient_profile', kwargs={'user_id': self.object.patient.user.pk})

    def form_valid(self, form):
        response = super(PatientFormBaseView, self).form_valid(form)

        # Send notification to doctors and clinics
        action_type = 'Save patient form'

        patient_user = get_object_or_404(User, pk=self.user_id)
        clinic_user = patient_user.patient.clinic.user
        bookings = Booking.objects.filter(patient_id=patient_user.pk).all()
        doctor_users = [booking.doctor.user for booking in bookings]

        doctor_users.append(clinic_user)
        targets = doctor_users or [clinic_user, ]
        print targets

        if targets:
            for target in targets:
                subject = self.request.user
                if target and not subject == target:
                    action = 'saved ' + str(self.object)
                    notification = Notification(
                        subject=subject,
                        action_type=action_type,
                        action=action,
                        target=target
                    )
                    notification.save()

        return response


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


class TMJScreeningView(PatientFormBaseView):
    template_name = 'medicalforms/patient_forms/tmj_screening.html'
    model = TMJScreening
    form_class = TMJScreeningForm


class LowerExtremityView(PatientFormBaseView):
    template_name = 'medicalforms/patient_forms/lower_extremity.html'
    model = LowerExtremity
    form_class = LowerExtremityForm


class UpperExtremityView(PatientFormBaseView):
    template_name = 'medicalforms/patient_forms/upper_extremity.html'
    model = UpperExtremity
    form_class = UpperExtremityForm


class NeckDisabilityView(PatientFormBaseView):
    template_name = 'medicalforms/patient_forms/neck_disability.html'
    model = NeckDisability
    form_class = NeckDisabilityForm


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
