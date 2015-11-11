from django.contrib.auth.models import Group

from test_plus.test import TestCase


class TestUser(TestCase):

    def setUp(self):
        self.user = self.make_user()

    def test__str__(self):
        self.assertEqual(
            self.user.__str__(),
            "testuser"  # This is the default username for self.make_user()
        )

    '''def test_get_absolute_url(self):
        self.assertEqual(
            self.user.get_absolute_url(),
            '/users/testuser/'
        )'''

    def test_add_to_patients_group(self):
        self.user.add_to_patients_group()
        self.assertTrue(
            self.user.groups.filter(name="Patients").exists()
        )

    def test_add_to_doctors_group(self):
        self.user.add_to_doctors_group()
        self.assertTrue(
            self.user.groups.filter(name="Doctors").exists()
        )
