from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from MedicalApp.users.models import User

from .patient_info_models import *
from .health_history_models import *
from .subjective_evaluation_models import *
from .assessment_models import *
from .accident_history_models import *

