# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, RedirectView, UpdateView, TemplateView
from django.shortcuts import redirect, get_object_or_404

from braces.views import LoginRequiredMixin, StaffuserRequiredMixin, GroupRequiredMixin
from allauth.account.views import LoginView, SignupView, FormView, PasswordChangeView
from allauth.account.utils import complete_signup
from allauth.account import app_settings

from .models import User
from MedicalAppointments.models import Patient, Doctor, Clinic
from .forms import UserSettingsForm, EmailDoctorForm, DoctorSettingsForm,\
    DoctorSignupForm, PatientSignupForm, PatientSettingsForm
from MedicalApp.utils import MultipleFormsView


class HomeView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        if self.request.user.groups.filter(name="Doctors").exists():
            return reverse("medical_appointments:timetable_doctor")
        elif self.request.user.groups.filter(name="Patients").exists():
            return reverse("medical_appointments:appointments")
        else:
            return reverse("users:manage_main")


class UserLoginView(LoginView):
    pass


class PatientSignupView(SignupView):
    template_name = "users/patient_signup.html"

    def get_form_class(self):
        return PatientSignupForm

    def form_valid(self, form):
        user = form.save(self.request)
        user.add_to_patients_group()
        patient = Patient(user=user)
        clinic = form.cleaned_data.get('clinic')
        if clinic:
            patient.clinic = clinic
        patient.save()
        return complete_signup(self.request, user,
                               app_settings.EMAIL_VERIFICATION,
                               self.get_success_url())


class DoctorSignupView(SignupView):
    template_name = "users/doctor_signup.html"

    def get_form_class(self):
        return DoctorSignupForm

    def form_valid(self, form):
        user = form.save(self.request)
        user.add_to_doctors_group()
        HCAI = form.cleaned_data.get('HCAI')
        doctor = Doctor(user=user)
        if HCAI:
            doctor.HCAI = HCAI
        doctor.save()
        return complete_signup(self.request, user,
                               app_settings.EMAIL_VERIFICATION,
                               self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(DoctorSignupView, self).get_context_data(**kwargs)
        context['doctors'] = True
        return context


class PatientProfileView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "pk"
    slug_url_kwarg = "user_id"
    template_name = "users/patient_profile.html"

    def get_context_data(self, **kwargs):
        context = super(PatientProfileView, self).get_context_data(**kwargs)
        if self.request.user.groups.filter(name="Doctors").exists() or self.request.user.is_staff or\
        self.request.user.groups.filter(name="Clinics").exists():
            context['form_access'] = True
        return context


class PatientProfileEditView(LoginRequiredMixin, MultipleFormsView):
    form_classes = {
        'user_settings': UserSettingsForm,
        'patient_settings': PatientSettingsForm
    }
    template_name = 'users/user_settings.html'

    def get_form_initial(self):
        self.user_id = self.kwargs['user_id']
        self.form_initial = {
            'user_settings': get_object_or_404(User, pk=self.user_id),
            'patient_settings': get_object_or_404(Patient, pk=self.user_id)
        }

    def get_context_data(self, **kwargs):
        context = super(PatientProfileEditView, self).get_context_data(**kwargs)
        context['patient_user'] = get_object_or_404(User, pk=self.user_id)
        return context

    def get_success_url(self):
        return reverse("users:patient_profile", kwargs={'user_id': self.kwargs['user_id']})

    def post(self, request, *args, **kwargs):
        if request.POST.get('Delete'):
            user = self.get_object()
            user.delete()
            return redirect(reverse('users:patient_list'))
        return super(PatientProfileEditView, self).post(request, *args, **kwargs)


class DoctorProfileView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "pk"
    slug_url_kwarg = "user_id"
    template_name = "users/doctor_profile.html"


class DoctorProfileEditView(LoginRequiredMixin, MultipleFormsView):
    template_name = "users/doctor_settings.html"

    form_classes = {
        'user_settings': UserSettingsForm,
        'doctor_settings': DoctorSettingsForm
    }

    def get_form_initial(self):
        self.user_id = self.kwargs['user_id']
        self.form_initial = {
            'user_settings': get_object_or_404(User, pk=self.user_id),
            'doctor_settings': get_object_or_404(Doctor, pk=self.user_id)
        }

    def get_context_data(self, **kwargs):
        context = super(DoctorProfileEditView, self).get_context_data(**kwargs)
        context['doctor_user'] = get_object_or_404(User, pk=self.user_id)
        print context['doctor_user']
        return context

    def post(self, request, *args, **kwargs):
        self.user_id = kwargs['user_id']
        if request.POST.get('Delete'):
            user = get_object_or_404(User, pk=self.user_id)
            user.delete()
            return redirect(reverse('users:doctors_list'))
        return super(DoctorProfileEditView, self).post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("users:doctor_profile", kwargs={"user_id": self.user_id})


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        if self.request.user.is_staff:
            return reverse('users:manage_main')
        elif self.request.user.groups.filter(name="Clinics").exists():
            clinic = get_object_or_404(Clinic, user=self.request.user)
            return reverse("medical_appointments:clinic_profile",
                       kwargs={"clinicname": clinic.name})
        else:
            return reverse("users:patient_doctor_redirect",
                           kwargs={"user_id": self.request.user.pk})


class PatientDoctorRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self, user_id):
        if self.request.user.groups.filter(name="Doctors").exists():
            return reverse("users:doctor_profile",
                       kwargs={"user_id": user_id})
        else:
            return reverse("users:patient_profile",
                           kwargs={"user_id": user_id})


class PatientsListView(LoginRequiredMixin, GroupRequiredMixin, ListView):
    model = Patient
    template_name = "users/patient_list.html"
    group_required = "Clinics"
    raise_exception = True


class ManageMainView(LoginRequiredMixin, GroupRequiredMixin, TemplateView):
    template_name = "users/manage_main.html"
    group_required = "Clinics"
    raise_exception = True


class DoctorsListView(LoginRequiredMixin, GroupRequiredMixin, ListView):
    model = Doctor
    template_name = "users/doctors_list.html"
    raise_exception = True
    group_required = "Clinics"

    def get_context_data(self, **kwargs):
        context = super(DoctorsListView, self).get_context_data(**kwargs)
        context['clinics'] = Clinic.objects.all()
        return context

    def get_queryset(self):
        queryset = super(DoctorsListView, self).get_queryset()
        clinic = self.request.GET.get('clinic', '')
        sortby = self.request.GET.get('sortby', '')
        if clinic:
            queryset = queryset.filter(clinic=clinic)
        if sortby == 'desc':
            return queryset.order_by('-user__last_name')
        else:
            return queryset.order_by('user__last_name')


class EmailDoctorView(LoginRequiredMixin, GroupRequiredMixin, FormView):
    template_name = "users/email_doctor.html"
    form_class = EmailDoctorForm
    success_url = reverse_lazy('users:doctors_list')
    group_required = "Clinics"

    def form_valid(self, form):
        signin_uri = self.request.build_absolute_uri(reverse("users:account_signup_doctors"))
        form.send_email(self.request.user.email, signin_uri)
        messages.add_message(self.request, messages.SUCCESS, 'Signup email sent to a doctor.')
        return super(EmailDoctorView, self).form_valid(form)


class UserPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy("users:account_logout")