from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from MedicalApp.users.models import User


SUBJECTIVE_CHOICES = (
    ('Reg.', 'Reg.'),
    ('Irreg.', 'Irreg.'),
    ('Pain/Cramps', 'Pain/Cramps')
)


# Assessment questions
@python_2_unicode_compatible
class Assessment(models.Model):
    user = models.ForeignKey(User)
    today_date = models.DateTimeField(auto_now_add=True, blank=True)
    date = models.DateTimeField(blank=True)
    visit_number = models.IntegerField(blank=True)
    clinician = models.CharField(max_length=100, blank=True)
    subjective_choices = models.CharField(max_length=15,
                                          choices=SUBJECTIVE_CHOICES,
                                          blank=True)
    subjective_description = models.TextField(blank=True)
    assessment = models.TextField(blank=True)
    objective = models.TextField(blank=True)
    smt = models.TextField(blank=True)
    stt = models.TextField(blank=True)
    cardio = models.CharField(max_length=100, blank=True)
    stretch = models.CharField(max_length=100, blank=True)
    strength = models.CharField(max_length=100, blank=True)
    ifc = models.CharField(max_length=100, blank=True)
    u_s = models.CharField(max_length=100, blank=True)
    heat = models.CharField(max_length=100, blank=True)
    ice = models.CharField(max_length=100, blank=True)
    ohter = models.TextField(blank=True)
    education = models.TextField(blank=True)

    def __str__(self):
        return 'Assessment for ' + self.user.first_name
        + ' ' + self.user.last_name
