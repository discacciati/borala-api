from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status

from events.models import Event

class EventListOneTest(APITestCase):
    fixtures = ["event-fixture.json"]

    @classmethod
    def setUpTestData(cls):
        cls.event  = Event.objects.all()[0]

        cls.client = APIClient()
    
    def test_should_list_single_event(self):
        response      = self.client.get(f"/api/events/{self.event.id}")
        response_dict = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response_dict["id"], str(self.event.id))
        self.assertEqual(response_dict["username"], self.event.username)
        self.assertEqual(response_dict["email"], self.event.email)
        self.assertEqual(response_dict["first_name"], self.event.first_name)
        self.assertEqual(response_dict["last_name"], self.event.last_name)
        self.assertEqual(response_dict["is_promoter"], self.event.is_promoter)