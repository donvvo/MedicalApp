from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from MedicalApp.users.models import User

from .model_folder.patient_models.patient_info_models import *
from .model_folder.patient_models.health_history_models import *
from .model_folder.patient_models.accident_history_models import *
from .model_folder.patient_models.tmj_screening_models import *
from .model_folder.patient_models.lower_extremity_models import *
from .model_folder.patient_models.upper_extremity_models import *
from .model_folder.patient_models.neck_disability_models import *
from .model_folder.patient_models.consent_form_models import *

from .subjective_evaluation_models import *
from .assessment_models import *
from .MVA_intake_models import *
from .report_of_findings_models import ReportOfFindings
from .acute_concussion_evaluation_models import AcuteConcussionEvaluation
from .plan_of_management_models import *
from .model_folder.patient_discharge_models import *
from .model_folder.doctor_models.patient_specific_functional_scale_models import *
from .model_folder.doctor_models.attendance_sheet_models import *

