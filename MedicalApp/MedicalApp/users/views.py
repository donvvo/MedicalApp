# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import datetime

from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, RedirectView, UpdateView, TemplateView
from django.views.generic.edit import FormView
from django.shortcuts import redirect, get_object_or_404
from django.utils import timezone

from braces.views import LoginRequiredMixin, StaffuserRequiredMixin, GroupRequiredMixin
from allauth.account.views import LoginView, SignupView, PasswordChangeView, PasswordResetView,\
     PasswordResetFromKeyView
from allauth.account.utils import complete_signup
from allauth.account import app_settings

from .models import User
from MedicalAppointments.models import Patient, Doctor, Clinic, Booking, NewForms
from MedicalAppointments.utils import get_time_table, get_clinic_time_table
from .forms import UserSettingsForm, EmailDoctorForm, DoctorSettingsForm,\
    DoctorSignupForm, PatientSignupForm, PatientSettingsForm, UserResetPasswordForm, UserResetPasswordKeyForm
from MedicalApp.utils import MultipleFormsView
from MedicalAppointments.forms import ClinicSettingsForm, NewFormsForm


class HomeView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "users/doctor_main.html"

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.groups.filter(name="Doctors").exists():
            return super(HomeView, self).dispatch(request, *args, **kwargs)
        elif self.request.user.groups.filter(name="Patients").exists():
            return redirect(reverse("medical_appointments:appointments"))
        elif self.request.user.groups.filter(name="Clinics").exists()\
                or self.request.user.is_staff:
            return redirect(reverse("users:manage_main"))
        else:
            return redirect(reverse("users:account_login"))

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        user = self.get_object()

        context['authorized'] = user == self.request.user

        doctor = get_object_or_404(Doctor, user=user)
        context['doctor'] = doctor

        context['patients'] = Patient.objects.filter(booking__doctor=doctor).distinct()

        bookings = Booking.objects.filter(doctor=doctor).all()
        context['bookings'] = bookings.filter(time__gte=timezone.now()).all()

        context['table'] = get_time_table(
            bookings, clinic=doctor.clinic, table_interval=30, num_doctor=1)

        return context


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


class UserPasswordResetView(PasswordResetView):
    template_name = "users/forgot_password.html"
    form_class = UserResetPasswordForm
    success_url = reverse_lazy("account_reset_password_done")


class PasswordResetDoneView(TemplateView):
    template_name = "account/password_reset_done.html"


class UserPasswordResetFromKeyView(PasswordResetFromKeyView):
    template_name = "users/password_reset_from_key.html"
    form_class = UserResetPasswordKeyForm


class PatientProfileView(LoginRequiredMixin, FormView):
    model = User
    form_class = NewFormsForm
    template_name = "users/patient_profile.html"

    def dispatch(self, request, *args, **kwargs):
        self.user = get_object_or_404(User, pk=kwargs['user_id'])

        return super(PatientProfileView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        new_forms = form.save(commit=False)
        new_forms.patient = self.user.patient
        new_forms.save()

        return super(PatientProfileView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(PatientProfileView, self).get_context_data(**kwargs)

        context['object'] = self.user

        if self.request.user.groups.filter(name="Doctors").exists() or self.request.user.is_staff or\
                self.request.user.groups.filter(name="Clinics").exists():
            context['form_access'] = True

        context['authorized'] = self.user == self.request.user or\
            self.request.user.is_staff or\
            self.request.user.groups.filter(name="Clinics").exists()

        patient = self.user.patient

        context['appointments'] = Booking.objects.filter(patient=patient,
                                                        time__gte=timezone.now()).order_by('time')

        context['new_forms'] = NewForms.objects.filter(patient=patient).all()

        context['patient'] = patient

        return context

    def get_success_url(self):
        return reverse('users:patient_profile', kwargs={'user_id': self.user.pk})


class PatientProfileEditView(LoginRequiredMixin, MultipleFormsView):
    form_classes = {
        'user_settings': UserSettingsForm,
        'patient_settings': PatientSettingsForm
    }
    template_name = 'users/user_profile_edit.html'

    def get_form_initial(self):
        self.user_id = self.kwargs['user_id']
        self.form_initial = {
            'user_settings': get_object_or_404(User, pk=self.user_id),
            'patient_settings': get_object_or_404(Patient, pk=self.user_id)
        }

    def get_context_data(self, **kwargs):
        context = super(PatientProfileEditView, self).get_context_data(**kwargs)
        context['user'] = get_object_or_404(User, pk=self.user_id)
        return context

    def get_success_url(self):
        return reverse("users:patient_profile", kwargs={'user_id': self.kwargs['user_id']})


class UserProfileEditView(LoginRequiredMixin, MultipleFormsView):
    form_classes = {
        'user_settings': UserSettingsForm,
    }
    template_name = 'users/user_profile_edit.html'

    
    def get_form_classes(self):
        form_classes = self.form_classes

        # Has UserSettingsForm as base. Additional forms are added depending on user group
        self.user_id = self.kwargs['user_id']
        self.user = get_object_or_404(User, pk=self.user_id)

        # Additional forms depending on user group
        if self.user.groups.filter(name="Patients").exists():
            form_classes['patient_settings'] = PatientSettingsForm

        return form_classes

    def get_form_initial(self):
        self.user_id = self.kwargs['user_id']
        self.form_initial = {
            'user_settings': get_object_or_404(User, pk=self.user_id),
        }

        # user group specific initial form values 
        if self.user.groups.filter(name="Patients").exists():
            self.form_initial['patient_settings'] = get_object_or_404(Patient, pk=self.user_id)

    def get_context_data(self, **kwargs):
        context = super(UserProfileEditView, self).get_context_data(**kwargs)
        self.user = get_object_or_404(User, pk=self.user_id)
        context['user'] = self.user
        return context

    def post(self, request, *args, **kwargs):
        form_classes = {
            'user_settings': UserSettingsForm,
        }

        self.user_id = self.kwargs['user_id']
        self.user = get_object_or_404(User, pk=self.user_id)

        # Additional forms depending on user group
        if self.user.groups.filter(name="Patients").exists():
            form_classes['patient_settings'] = PatientSettingsForm

        self.get_initial()
        forms = self.get_forms_with_request(request.POST, request.FILES, form_classes)
        if all([form.is_valid() for form in forms.values()]):
            return self.forms_valid(forms)
        else:
            return self.forms_invalid(forms)


    def get_success_url(self):
        self.user_id = self.kwargs['user_id']
        user = get_object_or_404(User, pk=self.user_id)

        if user.groups.filter(name="Patients").exists():
            return reverse("users:patient_profile", kwargs={'user_id': self.kwargs['user_id']})
        elif user.groups.filter(name="Doctors").exists():
            return reverse("users:doctor_profile", kwargs={"user_id": self.user_id})
        elif user.groups.filter(name="Clinics").exists():
            return reverse("medical_appointments:clinic_profile", kwargs={"user_id": self.user_id})


class DoctorProfileView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "pk"
    slug_url_kwarg = "user_id"
    template_name = "users/doctor_profile.html"

    def get_context_data(self, **kwargs):
        context = super(DoctorProfileView, self).get_context_data(**kwargs)

        user = self.get_object()

        context['authorized'] = user == self.request.user or\
            self.request.user.is_staff or\
            self.request.user.groups.filter(name="Clinics").exists()

        doctor = get_object_or_404(Doctor, user=user)
        context['doctor'] = doctor

        context['patients'] = Patient.objects.filter(booking__doctor=doctor).distinct()

        bookings = Booking.objects.filter(doctor=doctor).all()
        context['bookings'] = bookings.filter(time__gte=timezone.now()).all()

        context['table'] = get_time_table(
            bookings, clinic=doctor.clinic, table_interval=30, num_doctor=1)

        return context


class DoctorProfileEditView(LoginRequiredMixin, MultipleFormsView):
    template_name = "users/user_profile_edit.html"

    form_classes = {
        'user_settings': UserSettingsForm,
    }

    def get_form_initial(self):
        self.user_id = self.kwargs['user_id']
        self.form_initial = {
            'user_settings': get_object_or_404(User, pk=self.user_id),
        }

    def get_context_data(self, **kwargs):
        context = super(DoctorProfileEditView, self).get_context_data(**kwargs)
        context['user'] = get_object_or_404(User, pk=self.user_id)
        return context

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
                       kwargs={"user_id": self.request.user.pk})
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


class ManageMainView(LoginRequiredMixin, GroupRequiredMixin, ListView):
    template_name = "users/manage_main.html"
    group_required = "Clinics"
    raise_exception = True
    model = Booking

    def get_queryset(self):
        bookings = []

        if self.request.user.groups.filter(name="Clinics").exists():
            # Limit number of queries by getting only bookings that is in the future
            yesterday = datetime.datetime.now() - datetime.timedelta(days=1)

            bookings = self.model.objects.filter(clinic=self.request.user.clinic_set.get()).filter(time__gte=yesterday).all()

        return bookings

    def get_context_data(self, **kwargs):
        context = super(ManageMainView, self).get_context_data(**kwargs)

        if self.request.user.groups.filter(name="Clinics").exists():
            context['table'] = get_clinic_time_table(
                context['object_list'], clinic=self.request.user.clinic_set.get(), table_interval=30)

        return context


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


class SettingsView(LoginRequiredMixin, UpdateView):
    template_name = "users/settings.html"
    form_class = EmailDoctorForm

    def get_object(self):
        user = get_object_or_404(User, id=self.kwargs['user_id'])
        self.user = user

        if user.groups.filter(name="Doctors").exists():
            self.form_class = DoctorSettingsForm
            self.success_url = reverse("users:doctor_profile", kwargs={'user_id': self.kwargs['user_id']})
            return user.doctor
        elif user.groups.filter(name="Patients").exists():
            self.form_class = PatientSettingsForm
            self.success_url = reverse("users:patient_profile", kwargs={'user_id': self.kwargs['user_id']})
            return user.patient
        elif user.groups.filter(name="Clinics").exists():
            self.form_class = ClinicSettingsForm
            self.success_url = reverse("medical_appointments:clinic_profile",
                kwargs={'user_id': self.kwargs['user_id']})
            return user.clinic_set.get()
        else:
            self.form_class = UserSettingsForm
            return user

    def get_context_data(self, **kwargs):
        context = super(SettingsView, self).get_context_data(**kwargs)

        context['user'] = self.user

        return context

    def post(self, request, *args, **kwargs):
        self.user_id = kwargs['user_id']
        if request.POST.get('Delete'):
            user = get_object_or_404(User, pk=self.user_id)
            user.delete()
            return redirect(reverse("home"))
        return super(SettingsView, self).post(request, *args, **kwargs)


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


class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    success_url = reverse_lazy("users:account_logout")
