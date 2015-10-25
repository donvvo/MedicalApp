# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import logging

from django.contrib.auth.models import AbstractUser, Group
from django.core.urlresolvers import reverse
from django.utils.encoding import python_2_unicode_compatible

logger = logging.getLogger(__name__)

# Create two user groups: patients and doctors
patient_group = Group.objects.get_or_create(name='Patients')
doctor_group = Group.objects.get_or_create(name='Doctors')


@python_2_unicode_compatible
class User(AbstractUser):
    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
