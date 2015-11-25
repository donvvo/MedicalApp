import datetime
import pytz
import random

from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.urlresolvers import reverse
from django.http import HttpResponseBadRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.views.generic import DetailView, ListView, UpdateView, CreateView, TemplateView
from django.utils import timezone

from braces.views import LoginRequiredMixin, StaffuserRequiredMixin, GroupRequiredMixin

from .models import Booking, DoctorSpecialty, Clinic, Doctor
from .utils import get_clinics_by_specialty, get_time_table


class PatientOnlyMixin(LoginRequiredMixin, GroupRequiredMixin):
    group_required = 'Patients'
    raise_exception = True


# Create your views here.
class AppointmentView(PatientOnlyMixin, ListView):
    model = Booking
    template_name = "medicalappointments/appointment.html"

    def get_queryset(self):
        bookings = self.model.objects.filter(patient=self.request.user.patient, time__gte=timezone.now()).all()
        return bookings


class NewAppointmentView(PatientOnlyMixin, ListView):
    model = DoctorSpecialty
    template_name = "medicalappointments/new_appointment.html"


@login_required
def get_clinics(request):
    if request.method == 'GET':
        specialty = request.GET.get('specialty')
        clinics = get_clinics_by_specialty(specialty)
        return HttpResponse(serializers.serialize("json", clinics), content_type="application/json")
    return HttpResponseBadRequest()


class PatientTimetableView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = "medicalappointments/timetable_patient.html"

    def dispatch(self, request, *args, **kwargs):
        # Only patients can view
        if self.request.user.groups.filter(name="Patients").exists():
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
        bookings = self.model.objects.filter(clinic=self.clinic_name).all()

        specialty = self.kwargs.get('specialty').replace('+', ' ')

        self.doctors = Doctor.objects.filter(clinic=self.clinic_name, specialty=specialty).all()

        return bookings

    def get_context_data(self, **kwargs):
        context = super(PatientTimetableView, self).get_context_data(**kwargs)
        context['table'] = get_time_table(
            context['object_list'], table_start=6, table_end=17, table_interval=30, num_doctor=len(self.doctors))
        context['clinic'] = self.kwargs.get('clinic', None).replace('+', ' ')
        context['specialty'] = self.kwargs.get('specialty', None)

        return context

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            year = int(request.POST.get('year'))
            month = int(request.POST.get('month'))
            date = int(request.POST.get('date'))
            hour = int(request.POST.get('hour'))
            minute = int(request.POST.get('minute'))

            clinic_name = str(request.POST.get('clinic'))
            specialty = str(request.POST.get('specialty'))

            local_tz = timezone.get_default_timezone()
            TZ_UTC = pytz.utc

            booking_time = datetime.datetime(year=year, month=month, day=date,
                hour=hour, minute=minute, tzinfo=local_tz).astimezone(TZ_UTC)

            clinic = Clinic(pk=clinic_name)

            free_doctors = []
            for doctor in clinic.doctor_set.filter(specialty_id=specialty):
                if not (booking_time in [a.time for a in doctor.booking_set.all()]):
                    free_doctors.append(doctor)

            print free_doctors

            doctor = random.choice(free_doctors)
            print doctor
            booking = Booking(clinic=clinic, patient=request.user.patient, doctor=doctor, time=booking_time)
            booking.save()

            return HttpResponseRedirect(reverse("medical_appointments:appointments"))


class DoctorTimetableView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = "medicalappointments/timetable_doctor.html"

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
            context['object_list'], table_start=6, table_end=17, table_interval=30, num_doctor=1)

        return context


class ClinicListView(LoginRequiredMixin, ListView):
    model = Clinic
    template_name = "medicalappointments/clinic_list.html"


class ClinicProfileView(LoginRequiredMixin, DetailView):
    model = Clinic
    template_name = "medicalappointments/clinic_profile.html"

    def get_object(self):
        clinic_name = self.kwargs['clinicname']
        clinic_name = clinic_name.replace('+', ' ')
        return get_object_or_404(self.model, name=clinic_name)


class ClinicProfileEditView(LoginRequiredMixin, UpdateView):
    model = Clinic
    template_name = "medicalappointments/clinic_edit.html"
    fields = ('name', 'phone', 'email', 'description', 'city', 'address', 'postal_code',
        'start_time', 'end_time')

    def get_object(self):
        clinic_name = self.kwargs['clinicname']
        clinic_name = clinic_name.replace('+', ' ')
        return get_object_or_404(self.model, name=clinic_name)

    def post(self, request, *args, **kwargs):
        if request.POST.get('Delete'):
            clinic = self.get_object()
            clinic.delete()
            return redirect(reverse('medical_appointments:clinic_list'))
        elif request.POST.get('DeleteDoctor'):
            doctor = get_object_or_404(Doctor, user_id=request.POST.get('doctor_id'))
            print doctor
            doctor.clinic = None
            doctor.save()

            return redirect(reverse('medical_appointments:clinic_profile_edit', kwargs={'clinicname': self.kwargs['clinicname']}))
        return super(ClinicProfileEditView, self).post(request, *args, **kwargs)


class ClinicProfileCreateView(LoginRequiredMixin, CreateView):
    model = Clinic
    template_name = "medicalappointments/clinic_create.html"
    fields = ('name', 'phone', 'email', 'description', 'city', 'address', 'postal_code',
        'start_time', 'end_time')


class AddDoctorView(LoginRequiredMixin, StaffuserRequiredMixin, TemplateView):
    raise_exception = True
    template_name = "medicalappointments/add_doctor.html"

    def get_context_data(self, **kwargs):
        context = super(AddDoctorView, self).get_context_data()
        clinic_name = kwargs['clinicname']
        context['clinic_name'] = clinic_name
        doctors = Doctor.objects.exclude(clinic=clinic_name.replace('+', ' '))
        print doctors
        context['doctors'] = doctors

        return context

    def post(self, request, *args, **kwargs):
        doctor = get_object_or_404(Doctor, user=request.POST.get('doctor'))
        clinic_name = kwargs['clinicname']
        clinic = get_object_or_404(Clinic, name=clinic_name.replace('+', ' '))
        doctor.clinic = clinic
        doctor.save()

        return redirect(reverse('medical_appointments:clinic_profile', kwargs={'clinicname': clinic_name}))

