import uuid

from events.models import Event
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status
from users.models import User


class CreateEventTest(APITestCase):
    fixtures = [
        "user-fixture.json",
        "event-fixture.json",
        "address-fixture.json",
        "category-fixture.json",
    ]

    @classmethod
    def setUpTestData(cls):
        cls.promoter = User.objects.filter(is_promoter=True)[0]
        cls.other_user = User.objects.filter(is_promoter=False)[0]

        cls.event_data_no_address = {
            "title": "festa no ape",
            "date": "2022-09-07",
            "description": "vai rolar bunda-lele",
        }

        cls.event_data = {
            "title": "festa no ape",
            "date": "2022-09-07",
            "description": "vai rolar bunda-lele",
            "address": {
                "state": "BA",
                "city": "Salvador",
                "postal_code": "64260-000",
                "street": "Antenor de Araujo Freitas",
                "district": "Centro",
                "number": 1905,
            },
            "categories": [{"name": "Show"}],
        }

        cls.client = APIClient()

    def test_should_create_event(self):
        token, _ = Token.objects.get_or_create(user_id=self.promoter.id)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        response = self.client.post("/api/events/", self.event_data, format="json")

        response_dict = response.json()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(uuid.UUID(response_dict["id"]))

        event = Event.objects.get(id=response_dict["id"])

        self.assertEqual(response_dict["title"], self.event_data["title"])
        self.assertEqual(response_dict["date"], self.event_data["date"])
        self.assertEqual(response_dict["description"], self.event_data["description"])

        self.assertEqual(response_dict["title"], event.title)
        self.assertEqual(response_dict["date"], str(event.date))
        self.assertEqual(response_dict["description"], event.description)

        self.assertTrue(response_dict["is_active"])
        self.assertTrue(event.is_active)

    def test_should_not_create_event_without_data(self):
        token, _ = Token.objects.get_or_create(user_id=self.promoter.id)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        response = self.client.post("/api/events/", {})
        response_dict = response.json()

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertIn("title", response_dict.keys())
        self.assertIn("date", response_dict.keys())

    def test_should_not_create_event_without_permission(self):
        token, _ = Token.objects.get_or_create(user_id=self.other_user.id)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        response = self.client.post("/api/events/", self.event_data, format="json")

        response_dict = response.json()

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.assertIn("detail", response_dict.keys())

    def test_should_not_create_event_without_token(self):

        response = self.client.post("/api/events/", self.event_data, format="json")

        response_dict = response.json()

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.assertIn("detail", response_dict.keys())
