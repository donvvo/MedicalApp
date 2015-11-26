import datetime
import pytz

from test_plus.test import TestCase

from django.utils import timezone

from .models import Clinic, Doctor, DoctorSpecialty, Booking, Patient
from .utils import get_clinics_by_specialty, check_booking_in_timeslot,\
    get_min_start_hour, get_max_end_hour, get_column_for_a_day

local_tz = timezone.get_default_timezone()


class TestUtils(TestCase):
    def setUp(self):
        clinics = []
        clinics.append(Clinic(name='test1', city='city1', address='address1', postal_code='postal1'))
        clinics.append(Clinic(name='test2', city='city2', address='address2', postal_code='postal2'))
        clinics.append(Clinic(name='test3', city='city3', address='address3', postal_code='postal3'))
        clinics.append(Clinic(name='test4', city='city4', address='address4', postal_code='postal4'))

        specialties = []
        specialties.append(DoctorSpecialty(specialty='specialty1'))
        specialties.append(DoctorSpecialty(specialty='specialty2'))

        doctors = []
        doctors.append(Doctor(user=self.make_user('user1'), specialty=specialties[0], clinic=clinics[0]))
        doctors.append(Doctor(user=self.make_user('user2'), specialty=specialties[0], clinic=clinics[1]))
        doctors.append(Doctor(user=self.make_user('user3'), specialty=specialties[1], clinic=clinics[0]))
        doctors.append(Doctor(user=self.make_user('user4'), specialty=specialties[1], clinic=clinics[2]))

        for clinic in clinics:
            clinic.save()

        for specialty in specialties:
            specialty.save()

        for doctor in doctors:
            doctor.save()

        self.clinics = clinics
        self.specialties = specialties
        self.doctors = doctors
        self.patient = Patient(user=self.make_user('user5'))

        self.start_end_hour = [
            (datetime.time(hour=6, tzinfo=local_tz), datetime.time(hour=8, tzinfo=local_tz)),
            (None, datetime.time(hour=8, tzinfo=local_tz)),
            (datetime.time(hour=6, tzinfo=local_tz), None),
            (None, None),
            (datetime.time(hour=5, tzinfo=local_tz), datetime.time(hour=8, tzinfo=local_tz)),
            (datetime.time(hour=6, tzinfo=local_tz), datetime.time(hour=9, tzinfo=local_tz)),
        ]

    def test_get_clinics_by_specialty(self):
        self.assertEqual(
            get_clinics_by_specialty('specialty1'),
            [self.clinics[0], self.clinics[1]]
        )
        self.assertEqual(
            get_clinics_by_specialty('specialty2'),
            [self.clinics[0], self.clinics[2]]
        )
        self.assertEqual(
            get_clinics_by_specialty('specialty3'),
            []
        )

    def test_check_booking_in_timeslot(self):
        interval = datetime.timedelta(hours=1)
        booking_time = []
        booking_time.append(timezone.now())
        booking_time.append(booking_time[0] + interval)
        booking_time.append(booking_time[0] + datetime.timedelta(minutes=30))

        self.assertEqual(
            check_booking_in_timeslot(booking_time[1] + interval, interval, booking_time),
            []
        )
        self.assertEqual(
            check_booking_in_timeslot(booking_time[0], interval, booking_time),
            [0, 2]
        )
        self.assertEqual(
            check_booking_in_timeslot(booking_time[1], interval, booking_time),
            [1]
        )

    def test_min_start_hour(self):
        self.assertEqual(
            get_min_start_hour(self.start_end_hour),
            datetime.time(hour=5, tzinfo=local_tz)
        )

    def test_max_end_hour(self):
        self.assertEqual(
            get_max_end_hour(self.start_end_hour),
            datetime.time(hour=9, tzinfo=local_tz)
        )

    def test_get_column_for_a_day(self):
        min_start_hour = get_min_start_hour(self.start_end_hour)
        max_end_hour = get_max_end_hour(self.start_end_hour)
        day = timezone.now().date()

        interval = datetime.timedelta(minutes=30)

        print get_column_for_a_day(day, self.start_end_hour[1], min_start_hour, max_end_hour,
            interval, [], 1)


