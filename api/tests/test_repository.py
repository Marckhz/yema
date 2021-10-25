from django.test import Client, TestCase

from ..fixtures.appointments import APPOINTMENTS_FIXTURE

PATHS = {
    "schedule":'/api/schedule'
}

class APITest(TestCase):
    
    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_post_appointment(self):
        c = Client()
        data = APPOINTMENTS_FIXTURE()
        path = PATHS['schedule']
        rv = c.post(path, data, content_type='application/json')
        assert rv.status_code == 201
