from events.models import Event
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status


class EventListTest(APITestCase):
    fixtures = [
        "user-fixture.json",
        "event-fixture.json",
        "address-fixture.json",
        "category-fixture.json",
    ]

    @classmethod
    def setUpTestData(cls):
        cls.events_list = Event.objects.all()
        cls.events_len = len(cls.events_list)

        cls.client = APIClient()

    def test_should_list_all_events(self):
        response = self.client.get("/api/events/")
        response_list = response.json()["results"]
        response_dict = {
            response_list[i]["id"]: resp for i, resp in enumerate(response_list)
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_list), self.events_len)

        for event in self.events_list:
            id_string = str(event.id)
            response_data = response_dict[id_string]

            self.assertEqual(response_data["id"], id_string)
            self.assertEqual(response_data["title"], event.title)
            self.assertEqual(response_data["date"], str(event.date))
            self.assertEqual(response_data["description"], event.description)
