from unittest.mock import patch

from django.contrib.admin.options import ModelAdmin
from django.contrib.admin.sites import AdminSite
from django.test import Client, TestCase

from api.tests.test_repository import APITest
from appointments.admin import AppointmentAdmin

#from yemasite.utils.email import send_email
from ..models import Appointment

APPOINTMENT = { }

class MockRequest:
    pass


class MockSuperUser:
    def has_perm(self, perm):
        return True

request = MockRequest()
request.user = MockSuperUser()

class TestAdminAppointmentSite(TestCase):
    
    def setUp(self) -> None:
        self.site = AdminSite()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_model_admin_appointment(self):
        ma = ModelAdmin(Appointment, self.site)
        self.assertEqual(str(ma), 'appointments.ModelAdmin')
    
    def test_update_appointment(self):
       APITest().test_post_appointment()
       # just iter for first object
       qs = Appointment.objects.all()
       ap = qs[0]
       self.assertIsInstance(ap,Appointment)
       ap.accepted = True
       ap.comments = "test"
       ap.doctor = "test"
       ap.save()
    
    @patch('appointments.admin.AppointmentAdmin.save_model')
    def test_send_email(self, send_mail_mock):
        APITest().test_post_appointment()
        qs = Appointment.objects.all()
        qs = qs[0]
        form = {'accepted':'True', 'comments':'No comments',
               'doctor':'test'}
        AppointmentAdmin.save_model(form,obj=Appointment,request=None,  change=None)
        send_mail_mock.assert_called()

