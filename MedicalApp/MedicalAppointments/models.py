from django.core.urlresolvers import reverse_lazy
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

from MedicalApp.users import models as users_model
from MedicalForms.utils import *


TRANSPORTATION_CHOICES = (
    ('Regular', 'Regular'),
    ('Wheelchair Accessible', 'Wheelchair Accessible')
)

@python_2_unicode_compatible
class Clinic(models.Model):
    name = MyCharField(max_length=100, primary_key=True, placeholder='Clinic Name')
    user = models.ForeignKey(users_model.User)
    phone = MyCharField(max_length=20, placeholder='Phone Number')
    description = MyTextField(placeholder='Description')
    city = MyCharField(max_length=20, placeholder='City')
    address = MyCharField(max_length=200, placeholder='Address')
    postal_code = MyCharField(max_length=10, placeholder='Postal Code')
    start_time_mon = MyTimeField(placeholder='Opening Hours')
    end_time_mon = MyTimeField(placeholder='Closing Hours')
    start_time_tue = MyTimeField(placeholder='Opening Hours')
    end_time_tue = MyTimeField(placeholder='Closing Hours')
    start_time_wed = MyTimeField(placeholder='Opening Hours')
    end_time_wed = MyTimeField(placeholder='Closing Hours')
    start_time_thurs = MyTimeField(placeholder='Opening Hours')
    end_time_thurs = MyTimeField(placeholder='Closing Hours')
    start_time_fri = MyTimeField(placeholder='Opening Hours')
    end_time_fri = MyTimeField(placeholder='Closing Hours')
    start_time_sat = MyTimeField(placeholder='Opening Hours')
    end_time_sat = MyTimeField(placeholder='Closing Hours')
    start_time_sun = MyTimeField(placeholder='Opening Hours')
    end_time_sun = MyTimeField(placeholder='Closing Hours')

    def __str__(self):
        return self.name

    def url_name(self):
        return self.name.replace(' ', '+')

    def get_absolute_url(self):
        return reverse_lazy('medical_appointments:clinic_profile', kwargs={'clinicname': self.url_name()})


@python_2_unicode_compatible
class DoctorSpecialty(models.Model):
    specialty = models.CharField(max_length=20, primary_key=True)
    image_url = models.CharField(max_length=50, default='img/features/featured-2.jpg')

    def __str__(self):
        return self.specialty


@python_2_unicode_compatible
class Doctor(models.Model):
    user = models.OneToOneField(users_model.User, primary_key=True)
    specialty = models.ForeignKey(DoctorSpecialty, blank=True, null=True)
    clinic = models.ForeignKey(Clinic, blank=True, null=True, on_delete=models.SET_NULL)
    HCAI = MyCharField(max_length=30)

    def __str__(self):
        return str(self.user) + ' -- ' + 'Specialty: ' + str(self.specialty)


@python_2_unicode_compatible
class Patient(models.Model):
    user = models.OneToOneField(users_model.User, primary_key=True)
    clinic = models.ForeignKey(Clinic, blank=True, null=True, on_delete=models.SET_NULL)
    transportation_need = MySelectField(max_length=30, choices=TRANSPORTATION_CHOICES, default="Regular")
    past_medications = MyCharField(max_length=200, placeholder="Please type-in any past medications")
    current_medications = MyCharField(max_length=200, placeholder="Please type-in any current medications")
    height = MyCharField(max_length=30, placeholder="Height")
    weight = MyCharField(max_length=30, placeholder="Weight")
    smoking = MyNullBooleanField()
    alcohol = MyNullBooleanField()
    marijuana = MyNullBooleanField()

    def __str__(self):
        return str(self.user)


@python_2_unicode_compatible
class Booking(models.Model):
    clinic = models.ForeignKey(Clinic)
    patient = models.ForeignKey(Patient)
    doctor = models.ForeignKey(Doctor)
    time = models.DateTimeField()
    check_in = models.BooleanField(default=False)
    reasons = MyTextField(placeholder="Please write reasons for this appointment")
    symptoms = MyTextField(placeholder="Please write current symptoms")
    doctors_note = MyTextField(placeholder="Doctor's note")

    def __str__(self):
        return "Booking at " + self.clinic.pk + " at " + \
        timezone.localtime(self.time).strftime('%H:%M -- %m/%d/%y') + \
        " for " + str(self.patient) + " with " + str(self.doctor)


@python_2_unicode_compatible
class NewForms(models.Model):
    patient = models.ForeignKey(Patient)
    new_form = models.FileField(upload_to='forms')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.new_form.url
