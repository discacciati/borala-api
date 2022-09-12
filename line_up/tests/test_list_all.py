from events.models import Event
from line_up.models import LineUp
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status
from django.db.models import Count


class LineupListTest(APITestCase):
    fixtures = [
        "user-fixture.json",
        "event-fixture.json",
        "address-fixture.json",
        "category-fixture.json",
        "lineup-fixture.json",
    ]

    @classmethod
    def setUpTestData(cls):
        cls.event       = Event.objects.annotate(lineup_count=Count('lineup')).filter(lineup_count__gt=0)[0]
        cls.lineup_list = LineUp.objects.filter(event_id=cls.event.id)
        cls.lineup_len  = len(cls.lineup_list)

        cls.client = APIClient()

    def test_should_list_whole_lineup(self):
        response = self.client.get(f"/api/events/{self.event.id}/lineup/")
        response_list = response.json()['results']
        response_dict = {
            response_list[i]["id"]: resp for i, resp in enumerate(response_list)
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_list), self.lineup_len)

        for lineup in self.lineup_list:
            id_string = str(lineup.id)
            response_data = response_dict[id_string]

            self.assertEqual(response_data["title"], lineup.title)
            self.assertEqual(response_data["hour"], str(lineup.hour))
            self.assertEqual(response_data["description"], lineup.description)
            self.assertEqual(response_data["talent"], lineup.talent)
