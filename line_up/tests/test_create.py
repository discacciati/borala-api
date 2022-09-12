import uuid

from events.models import Event
from line_up.models import LineUp
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status
from users.models import User


class CreateLineupTest(APITestCase):
    fixtures = [
        "user-fixture.json",
        "event-fixture.json",
        "address-fixture.json",
        "category-fixture.json",
    ]

    @classmethod
    def setUpTestData(cls):
        cls.event = Event.objects.all()[0]
        cls.promoter = User.objects.get(id=cls.event.user.id)
        cls.other_user = User.objects.filter(is_promoter=False)[0]

        cls.lineup_data = {
            "title": "Show da Daniela Mercury",
            "hour": "19:00:00",
            "description": "Daniela faz seu primeiro show em...",
            "talent": "Daniela Mercury",
        }

        cls.client = APIClient()

    def test_should_create_lineup(self):
        token, _ = Token.objects.get_or_create(user_id=self.promoter.id)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        response = self.client.post(
            f"/api/events/{self.event.id}/lineup/", self.lineup_data
        )
        response_dict = response.json()
        lineup = LineUp.objects.get(id=response_dict["id"])

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(uuid.UUID(response_dict["id"]))

        self.assertEqual(response_dict["title"], self.lineup_data["title"])
        self.assertEqual(response_dict["hour"], self.lineup_data["hour"])
        self.assertEqual(response_dict["description"], self.lineup_data["description"])
        self.assertEqual(response_dict["talent"], self.lineup_data["talent"])

        self.assertEqual(response_dict["title"], lineup.title)
        self.assertEqual(response_dict["hour"], str(lineup.hour))
        self.assertEqual(response_dict["description"], lineup.description)
        self.assertEqual(response_dict["talent"], lineup.talent)

    def test_should_not_create_lineup_without_data(self):
        token, _ = Token.objects.get_or_create(user_id=self.promoter.id)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        response = self.client.post(f"/api/events/{self.event.id}/lineup/", {})
        response_dict = response.json()

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertIn("title", response_dict.keys())
        self.assertIn("hour", response_dict.keys())

    def test_should_not_create_lineup_without_permission(self):
        token, _ = Token.objects.get_or_create(user_id=self.other_user.id)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        response = self.client.post(
            f"/api/events/{self.event.id}/lineup/", self.lineup_data
        )
        response_dict = response.json()

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.assertIn("detail", response_dict.keys())

    def test_should_not_create_lineup_without_token(self):
        response = self.client.post(
            f"/api/events/{self.event.id}/lineup/", self.lineup_data
        )
        response_dict = response.json()

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.assertIn("detail", response_dict.keys())
