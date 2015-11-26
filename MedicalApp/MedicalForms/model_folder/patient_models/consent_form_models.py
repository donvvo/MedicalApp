from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from ...utils import *
from MedicalAppointments.models import Patient


@python_2_unicode_compatible
class ChiropracticTreatment(models.Model):
    patient = models.OneToOneField(Patient, primary_key=True)
    signature = MyCharField(max_length=50)
    date = MyDateTimeField()
    name = MyCharField(max_length=50)

    def __str__(self):
        return 'Chiropractic Treatment Consent for ' + str(self.patient)


@python_2_unicode_compatible
class PhysiotherapyTreatment(models.Model):
    patient = models.OneToOneField(Patient, primary_key=True)
    signature = MyCharField(max_length=50)
    date = MyDateTimeField()
    name = MyCharField(max_length=50)

    def __str__(self):
        return 'Physiotherapy Treatment Consent for ' + str(self.patient)


@python_2_unicode_compatible
class MassageTreatment(models.Model):
    patient = models.OneToOneField(Patient, primary_key=True)
    signature = MyCharField(max_length=50)
    date = MyDateTimeField()
    name = MyCharField(max_length=50)

    def __str__(self):
        return 'Masssage Treatment Consent for ' + str(self.patient)


@python_2_unicode_compatible
class MedicalAuthorization(models.Model):
    patient = models.OneToOneField(Patient, primary_key=True)
    TO = MyCharField(max_length=100)
    RE = MyCharField(max_length=100)
    date = MyDateTimeField()
    patient_signature = MyCharField(max_length=50)
    witness_signature = MyCharField(max_length=50)

    def __str__(self):
        return 'Medical Authorization for ' + str(self.patient)


@python_2_unicode_compatible
class ExchangeInformation(models.Model):
    patient = models.OneToOneField(Patient, primary_key=True)
    physician_name = MyCharField(max_length=50)
    physician_address = MyCharField(max_length=50)
    physician_phone = MyCharField(max_length=50)
    physician_fax = MyCharField(max_length=50)

    patient_name = MyCharField(max_length=50)
    patient_dob = MyCharField(max_length=50)

    representative_name1 = MyCharField(max_length=50)
    forward_from_name = MyCharField(max_length=50)
    include_notes = MyNullBooleanField()

    signature = MyCharField(max_length=50)
    date = MyDateTimeField()

    representative_name2 = MyCharField(max_length=50)
    representative_relationship = MyCharField(max_length=50)

    TO = MyCharField(max_length=100)
    RE = MyCharField(max_length=100)
    date = MyDateTimeField()
    patient_signature = MyCharField(max_length=50)
    witness_signature = MyCharField(max_length=50)

    def __str__(self):
        return 'Exchange of Medical Information for ' + str(self.patient)


@python_2_unicode_compatible
class AuthorizationAndDirection(models.Model):
    patient = models.OneToOneField(Patient, primary_key=True)
    TO = MyCharField(max_length=100)
    FROM = MyCharField(max_length=100)
    patient_name = MyCharField(max_length=100)
    automobile_insurer = MyCharField(max_length=100)
    claim_policy_number = MyCharField(max_length=100)
    date_of_loss = MyDateTimeField()
    SIN = MyCharField(max_length=100)
    legal_representative = MyCharField(max_length=100)
    primary_insurer = MyCharField(max_length=100)
    authorize_name = MyCharField(max_length=100)

    date = MyDateTimeField()
    patient_signature = MyCharField(max_length=100)
    witness_name = MyCharField(max_length=100)
    witness_signature = MyCharField(max_length=100)

    def __str__(self):
        return 'Authorization and Direction for ' + str(self.patient)


@python_2_unicode_compatible
class Section47(models.Model):
    patient = models.OneToOneField(Patient, primary_key=True)
    date = MyDateTimeField()
    patient_name = MyCharField(max_length=100)
    patient_signature = MyCharField(max_length=100)
    witness_name = MyCharField(max_length=100)
    witness_signature = MyCharField(max_length=100)

    def __str__(self):
        return 'Section 47 for ' + str(self.patient)


@python_2_unicode_compatible
class StatutoryAccidentsBenefits(models.Model):
    patient = models.OneToOneField(Patient, primary_key=True)
    date = MyDateTimeField()
    patient_name = MyCharField(max_length=100)
    patient_signature = MyCharField(max_length=100)
    witness_name = MyCharField(max_length=100)
    witness_signature = MyCharField(max_length=100)

    def __str__(self):
        return 'Statutory Accidents Benefits for ' + str(self.patient)
