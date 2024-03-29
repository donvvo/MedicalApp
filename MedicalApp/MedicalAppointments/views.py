import datetime
import pytz
import random

from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.urlresolvers import reverse
from django.http import HttpResponseBadRequest, HttpResponse, HttpResponseRedirect
from django.forms.models import model_to_dict
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.views.generic import DetailView, ListView, UpdateView, CreateView, TemplateView
from django.utils import timezone
from django.utils.decorators import method_decorator


from braces.views import LoginRequiredMixin, StaffuserRequiredMixin, GroupRequiredMixin
from allauth.account.utils import complete_signup
from allauth.account import app_settings

from .models import Booking, DoctorSpecialty, Clinic, Doctor, Patient, NewForms
from .utils import get_clinics_by_specialty, get_time_table
from .forms import ClinicUserSignupForm, ClinicForm, ClinicUserSettingsForm, NewFormsForm
from MedicalApp.utils import MultipleFormsView, user_passes_test_with_kwargs
from MedicalApp.users.models import User


def clinic_or_staff(user, **kwargs):
    clinic_user = get_object_or_404(User, id=kwargs['user_id'])
    return user.is_staff or \
        (user.groups.filter(name="Clinics").exists() and user == clinic_user)


class PatientOnlyMixin(LoginRequiredMixin, GroupRequiredMixin):
    group_required = 'Patients'
    raise_exception = True


# Create your views here.
class AppointmentView(PatientOnlyMixin, ListView):
    model = Booking
    template_name = "medicalappointments/appointment.html"

    def get_queryset(self):
        bookings = self.model.objects.filter(patient=self.request.user.patient, time__gte=timezone.now()).order_by('time')
        return bookings


class NewAppointmentView(LoginRequiredMixin, ListView):
    model = DoctorSpecialty
    group_required = ['Patients', 'Clinics']
    raise_exception = True
    template_name = "medicalappointments/new_appointment.html"

    def dispatch(self, request, *args, **kwargs):
        self.user_id = kwargs['user_id']
        return super(NewAppointmentView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(NewAppointmentView, self).get_context_data(**kwargs)

        context['user_id'] = self.user_id

        return context


@login_required
def get_clinics(request):
    if request.method == 'GET':
        specialty = request.GET.get('specialty')
        clinics = get_clinics_by_specialty(specialty)
        clinics_json = serializers.serialize("json", clinics) if clinics else '[]'
        return HttpResponse(clinics_json, content_type="application/json")
    return HttpResponseBadRequest()


class PatientTimetableView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = "medicalappointments/timetable_patient.html"

    def dispatch(self, request, *args, **kwargs):
        # Only patients can view
        if self.request.user.groups.filter(name="Patients").exists() or\
                self.request.user.groups.filter(name="Clinics").exists() or\
                self.request.user.is_staff:
            self.clinic_name = kwargs.get('clinic', '').replace('+', ' ')
            if not Clinic.objects.filter(name=self.clinic_name).exists():
                redirect_url = reverse("medical_appointments:new_appointments")
                return redirect(redirect_url)
            return super(PatientTimetableView, self).dispatch(request,
                                                         *args, **kwargs)
        else:
            redirect_url = reverse("users:account_redirect")
            return redirect(redirect_url)

    def get_queryset(self):
        bookings = self.model.objects.filter(clinic__name=self.clinic_name).all()

        specialty = self.kwargs.get('specialty').replace('+', ' ')

        self.doctors = Doctor.objects.filter(clinic__name=self.clinic_name, specialty=specialty).all()

        return bookings

    def get_context_data(self, **kwargs):
        context = super(PatientTimetableView, self).get_context_data(**kwargs)
        clinic = get_object_or_404(Clinic, name=self.clinic_name)
        context['table'] = get_time_table(
            context['object_list'], clinic=clinic, table_interval=30, num_doctor=len(self.doctors))
        context['clinic'] = self.kwargs.get('clinic', None).replace('+', ' ')
        context['specialty'] = self.kwargs.get('specialty', None)
        context['user_id'] = self.kwargs.get('user_id')

        return context

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            year = int(request.POST.get('year'))
            month = int(request.POST.get('month'))
            date = int(request.POST.get('date'))
            hour = int(request.POST.get('hour'))
            minute = int(request.POST.get('minute'))

            clinic_name = str(request.POST.get('clinic'))
            specialty = str(request.POST.get('specialty')).replace('+', ' ')

            local_tz = timezone.get_default_timezone()
            TZ_UTC = pytz.utc

            booking_time = datetime.datetime(year=year, month=month, day=date,
                hour=hour, minute=minute, tzinfo=local_tz).astimezone(TZ_UTC)

            clinic = get_object_or_404(Clinic, name=self.clinic_name)

            free_doctors = []
            for doctor in clinic.doctor_set.filter(specialty_id=specialty):
                if not (booking_time in [a.time for a in doctor.booking_set.all()]):
                    free_doctors.append(doctor)

            print 'free_doctors'
            print free_doctors

            doctor = random.choice(free_doctors)
            print 'Chosen doctor'
            print doctor

            patient = get_object_or_404(Patient, user_id=kwargs['user_id'])
            booking = Booking(clinic=clinic, patient=patient, doctor=doctor, time=booking_time)
            booking.save()

            if request.user.groups.filter(name='Patients').exists():
                return HttpResponseRedirect(reverse("medical_appointments:appointments"))
            else:
                return HttpResponseRedirect(reverse("users:patient_profile", kwargs={'user_id': kwargs['user_id']}))


class DoctorTimetableView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = "medicalappointments/timetable_doctor_old.html"

    def dispatch(self, request, *args, **kwargs):
        # Only patients can view
        if self.request.user.groups.filter(name="Doctors").exists():
            return super(DoctorTimetableView, self).dispatch(request,
                                                         *args, **kwargs)
        else:
            redirect_url = reverse("users:account_redirect")
            return redirect(redirect_url)

    def get_queryset(self):
        bookings = self.model.objects.filter(doctor=self.request.user.doctor).all()
        return bookings

    def get_context_data(self, **kwargs):
        context = super(DoctorTimetableView, self).get_context_data(**kwargs)
        context['table'] = get_time_table(
            context['object_list'], clinic=self.request.user.doctor.clinic, table_interval=30, num_doctor=1)

        return context


class ClinicListView(LoginRequiredMixin, StaffuserRequiredMixin, ListView):
    raise_exception = True
    model = Clinic
    template_name = "medicalappointments/clinic_list.html"


class ClinicProfileView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "pk"
    slug_url_kwarg = "user_id"
    template_name = "medicalappointments/clinic_profile.html"

    def get_context_data(self, **kwargs):
        context = super(ClinicProfileView, self).get_context_data(**kwargs)

        user = self.get_object()

        context['authorized'] = user == self.request.user or\
            self.request.user.is_staff

        clinic = get_object_or_404(Clinic, user=user)
        context['patients'] = Patient.objects.filter(clinic=clinic).all()

        context['clinic'] = clinic

        return context


class ClinicProfileEditView(LoginRequiredMixin, UpdateView):
    model = Clinic
    template_name = "medicalappointments/clinic_edit.html"
    fields = ('name', 'phone', 'description', 'city', 'address', 'postal_code',
        'start_time_mon', 'end_time_mon', 'start_time_tue', 'end_time_tue',
        'start_time_wed', 'end_time_wed', 'start_time_thurs', 'end_time_thurs',
        'start_time_fri', 'end_time_fri', 'start_time_sat', 'end_time_sat',
        'start_time_sun', 'end_time_sun')

    @method_decorator(user_passes_test_with_kwargs(clinic_or_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(ClinicProfileEditView, self). dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ClinicProfileEditView, self).get_context_data(**kwargs)

        clinic = self.get_object()
        initial = clinic.user
        context['user_form'] = ClinicUserSettingsForm(model_to_dict(initial))
        context['initial_image'] = clinic.user.image
        print context['user_form']
        return context

    def get_object(self):
        clinic_name = self.kwargs['clinicname']
        clinic_name = clinic_name.replace('+', ' ')
        return get_object_or_404(self.model, name=clinic_name)

    def form_valid(self, form):
        clinic = self.get_object()
        initial = clinic.user
        user_form = ClinicUserSettingsForm(self.request.POST, self.request.FILES, instance=initial)
        if user_form.is_valid():
            user_form.save()
        return super(ClinicProfileEditView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        if request.POST.get('Delete'):
            clinic = self.get_object()
            clinic.delete()
            return redirect(reverse('medical_appointments:clinic_list'))
        elif request.POST.get('DeleteDoctor'):
            doctor = get_object_or_404(Doctor, user_id=request.POST.get('doctor_id'))
            doctor.clinic = None
            doctor.save()

            return redirect(reverse('medical_appointments:clinic_profile_edit', kwargs={'clinicname': self.kwargs['clinicname']}))
        return super(ClinicProfileEditView, self).post(request, *args, **kwargs)


class ClinicProfileCreateView(LoginRequiredMixin, StaffuserRequiredMixin, MultipleFormsView):
    raise_exception = True
    template_name = "medicalappointments/clinic_create.html"
    form_classes = {
        'user_signup': ClinicUserSignupForm,
        'clinic_signup': ClinicForm
    }

    def get_form_initial(self):
        user = User()
        self.form_initial = {
            'user': user,
            'clinic': Clinic(user=user)
        }

    def forms_valid(self, forms):
        user_form = forms['user_signup']
        user = user_form.save(self.request)
        clinic = self.form_classes['clinic_signup'](self.request.POST, instance=Clinic(user=user))
        clinic = clinic.save()
        user.first_name = 'Clinic Admin'
        user.add_to_clinics_group()
        user.image = user_form.cleaned_data['image']
        user.save()

        return complete_signup(self.request, user,
                       app_settings.EMAIL_VERIFICATION,
                       self.get_success_url())

    def get_success_url(self):
        return reverse("home")


class AddDoctorView(LoginRequiredMixin, GroupRequiredMixin, TemplateView):
    template_name = "medicalappointments/add_doctor.html"
    group_required = "Clinics"

    def get_context_data(self, **kwargs):
        context = super(AddDoctorView, self).get_context_data()
        clinic_user = get_object_or_404(User, id=kwargs['user_id'])
        clinic = clinic_user.clinic
        context['clinic_name'] = clinic.name
        context['user_id'] = kwargs['user_id']
        doctors = Doctor.objects.exclude(clinic=clinic)
        context['doctors'] = doctors

        return context

    def post(self, request, *args, **kwargs):
        doctor = get_object_or_404(Doctor, user=request.POST.get('doctor'))
        clinic_user = get_object_or_404(User, id=kwargs['user_id'])
        clinic = clinic_user.clinic
        doctor.clinic = clinic
        doctor.save()

        return redirect(reverse('medical_appointments:clinic_profile', kwargs={'user_id': kwargs['user_id']}))


class AppointmentInfoView(LoginRequiredMixin, UpdateView):
    template_name = "medicalappointments/appointment_info.html"
    model = Booking
    slug_field = "pk"
    slug_url_kwarg = "booking_id"
    fields = ('check_in', 'reasons', 'symptoms', 'doctors_note')

    def get_context_data(self, **kwargs):
        context = super(AppointmentInfoView, self).get_context_data(**kwargs)
        if self.request.user.groups.filter(name="Doctors").exists() or self.request.user.is_staff or\
                self.request.user.groups.filter(name="Clinics").exists():
            context['form_access'] = True

        context['booking'] = context['object']
        context['object'] = self.get_object().patient.user
        context['new_forms'] = NewForms.objects.filter(patient=self.get_object().patient).all()

        context['new_forms_form'] = NewFormsForm

        return context

    def get_success_url(self):
        if self.request.user.groups.filter(name="Patients").exists():
            return reverse('medical_appointments:appointments')
        else:
            return reverse('users:doctor_profile', kwargs={'user_id': self.get_object().doctor.user_id})

    def form_valid(self, form):
        new_forms_form = NewFormsForm(self.request.POST, self.request.FILES)
        if new_forms_form.is_valid():
            new_forms = new_forms_form.save(commit=False)
            new_forms.patient = self.get_object().patient
            new_forms.save()
        return super(AppointmentInfoView, self).form_valid(form)

