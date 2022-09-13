from events.models import Event
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status


class EventListOneTest(APITestCase):
    fixtures = [
        "user-fixture.json",
        "event-fixture.json",
        "address-fixture.json",
        "category-fixture.json",
    ]

    @classmethod
    def setUpTestData(cls):
        cls.event = Event.objects.all()[0]

        cls.client = APIClient()

    def test_should_list_single_event(self):
        response = self.client.get(f"/api/events/{self.event.id}/")
        response_dict = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response_dict["id"], str(self.event.id))
        self.assertEqual(response_dict["title"], self.event.title)
        self.assertEqual(response_dict["date"], str(self.event.date))
        self.assertEqual(response_dict["description"], self.event.description)
