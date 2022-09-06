import uuid
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token

from users.models import User
from events.models import Event

class CreateEventTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.promoter   = User.objects.get(is_promoter=True)
        cls.other_user = User.objects.get(is_promoter=False)

        cls.event_data = {
            "name":"festa no ape",
            "date":"2022-09-07",
            "description":"vai rolar bunda-lele",
        }

        cls.client = APIClient()
    
    def test_should_create_user(self):
        token,_ = Token.objects.get_or_create(user_id=self.promoter.id)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        response      = self.client.post('/api/events/', self.event_data)
        response_dict = response.json()
        event         = Event.objects.get(id=response_dict["id"])

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(uuid.UUID(response_dict["id"]))

        self.assertEqual(response_dict["name"], self.event_data["name"])
        self.assertEqual(response_dict["date"], self.event_data["date"])
        self.assertEqual(response_dict["description"], self.event_data["description"])

        self.assertEqual(response_dict["name"], event.name)
        self.assertEqual(response_dict["date"], event.date)
        self.assertEqual(response_dict["description"], event.description)

        self.assertTrue(response_dict["is_active"])
        self.assertTrue(event.is_active)

    def test_should_not_create_event_without_data(self):
        token,_ = Token.objects.get_or_create(user_id=self.promoter.id)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        response      = self.client.post('/api/events/', {})
        response_dict = response.json()

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertIn("name", response_dict.keys())
        self.assertIn("date", response_dict.keys())
    
    def test_should_not_create_event_without_permission(self):
        token,_ = Token.objects.get_or_create(user_id=self.other_user.id)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        response      = self.client.post('/api/events/', self.event_data)
        response_dict = response.json()

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.assertIn("detail", response_dict.keys())
    
    def test_should_not_create_event_without_token(self):
        response      = self.client.post('/api/events/', self.event_data)
        response_dict = response.json()

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.assertIn("detail", response_dict.keys())