from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status

from events.models import Event
from line_up.models import Lineup

class LineupListOneTest(APITestCase):
    fixtures = ["event-fixture.json", "lineup-fixture.json"]

    @classmethod
    def setUpTestData(cls):
        cls.event  = Event.objects.all()[0]
        cls.lineup = Lineup.objects.filter(event_id=cls.event.id)[0]

        cls.client = APIClient()
    
    def test_should_list_single_lineup(self):
        response      = self.client.get(f"/api/events/{self.event.id}/lineup/{self.lineup.id}")
        response_dict = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response_dict["title"], self.lineup.title)
        self.assertEqual(response_dict["hour"], self.lineup.hour)
        self.assertEqual(response_dict["description"], self.lineup.description)
        self.assertEqual(response_dict["talent"], self.lineup.talent)