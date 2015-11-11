import datetime

from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.urlresolvers import reverse
from django.http import HttpResponseBadRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.views.generic import DetailView, ListView, TemplateView
from django.utils import timezone

from braces.views import LoginRequiredMixin

from .models import Booking, DoctorSpecialty, Clinic, Doctor
from .utils import get_clinics_by_specialty, get_time_table


# Create your views here.
class AppointmentView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = "medicalappointments/appointment.html"

    def dispatch(self, request, *args, **kwargs):
        # Only patients can view
        if self.request.user.groups.filter(name="Patients").exists():
            return super(AppointmentView, self).dispatch(request,
                                                         *args, **kwargs)
        else:
            redirect_url = reverse("users:account_redirect")
            return redirect(redirect_url)

    def get_queryset(self):
        bookings = self.model.objects.filter(patient=self.request.user.patient).all()
        return bookings


class NewAppointmentView(LoginRequiredMixin, ListView):
    model = DoctorSpecialty
    template_name = "medicalappointments/new_appointment.html"

    def dispatch(self, request, *args, **kwargs):
        # Only patients can view
        if self.request.user.groups.filter(name="Patients").exists():
            return super(NewAppointmentView, self).dispatch(request,
                                                         *args, **kwargs)
        else:
            redirect_url = reverse("users:account_redirect")
            return redirect(redirect_url)


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

        specialty = self.kwargs.get('specialty', None)

        self.doctors = Doctor.objects.filter(clinic=self.clinic_name, specialty=specialty).all()

        return bookings

    def get_context_data(self, **kwargs):
        context = super(PatientTimetableView, self).get_context_data(**kwargs)
        context['table'] = get_time_table(
            context['object_list'], table_start=6, table_end=17, table_interval=30, num_doctor=len(self.doctors))
        context['clinic'] = self.kwargs.get('clinic', None).replace('+', ' ')

        return context


def save_booking(request):
    if request.method == 'POST':
        year = int(request.POST.get('year'))
        month = int(request.POST.get('month'))
        date = int(request.POST.get('date'))
        hour = int(request.POST.get('hour'))
        minute = int(request.POST.get('minute'))

        clinic_name = str(request.POST.get('clinic'))

        booking_time = datetime.datetime(year=year, month=month, day=date, hour=hour, minute=minute)

        timezone.make_aware(booking_time, timezone.get_current_timezone())

        clinic = Clinic(pk=clinic_name)
        doctor = Doctor(pk=10)
        booking = Booking(clinic=clinic, patient=request.user.patient, doctor=doctor, time=booking_time)
        booking.save()

        return HttpResponseRedirect(reverse("medical_appointments:appointments"))
    return HttpResponseBadRequest()


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


class ClinicProfileView(LoginRequiredMixin, DetailView):
    model = Clinic
    template_name = "medicalappointments/clinic_profile.html"
    slug_field = "name"
    slug_url_kwarg = "clinicname"

    def get_object(self):
        clinic_name = self.kwargs['clinicname']
        print clinic_name
        clinic_name = clinic_name.replace('+', ' ')
        print clinic_name
        return self.model.objects.get(name=clinic_name)
