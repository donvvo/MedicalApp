import datetime
import pytz

from test_plus.test import TestCase

from django.utils import timezone

from .models import Clinic, Doctor, DoctorSpecialty
from .utils import get_clinics_by_specialty, get_dates_from_now, check_booking_in_timeslot,\
get_time_table


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

    def test_get_dates_from_now(self):
        today = timezone.now().date()
        days = [today.day + day for day in range(7)]

        self.assertEqual(
            days,
            [date.day for date in get_dates_from_now()]
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

