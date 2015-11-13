from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from MedicalApp.users.models import User

from .patient_info_models import *
from .health_history_models import *
from .subjective_evaluation_models import *
from .assessment_models import *
from .accident_history_models import *
from .MVA_intake_models import *
from .report_of_findings_models import ReportOfFindings
from .tmj_screening_models import TMJScreening
from .acute_concussion_evaluation_models import AcuteConcussionEvaluation