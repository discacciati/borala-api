from events.models import Event
from line_up.models import LineUp
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status


class LineupListOneTest(APITestCase):
    fixtures = [
        "user-fixture.json",
        "event-fixture.json",
        "address-fixture.json",
        "category-fixture.json",
        "lineup-fixture.json",
    ]

    @classmethod
    def setUpTestData(cls):
        cls.event = Event.objects.all()[1]
        cls.lineup = LineUp.objects.filter(event_id=cls.event.id)[0]

        cls.client = APIClient()

    def test_should_list_single_lineup(self):
        response = self.client.get(
            f"/api/events/{self.event.id}/lineup/{self.lineup.id}/"
        )
        response_dict = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response_dict["title"], self.lineup.title)
        self.assertEqual(response_dict["hour"], str(self.lineup.hour))
        self.assertEqual(response_dict["description"], self.lineup.description)
        self.assertEqual(response_dict["talent"], self.lineup.talent)
