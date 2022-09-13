from events.models import Event
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status
from users.models import User


class DeleteEventTest(APITestCase):
    fixtures = [
        "user-fixture.json",
        "event-fixture.json",
        "address-fixture.json",
        "category-fixture.json",
        "lineup-fixture.json",
    ]

    @classmethod
    def setUpTestData(cls):
        cls.event = Event.objects.all()[0]
        cls.admin_user = User.objects.filter(is_superuser=True)[0]
        cls.user = User.objects.filter(is_staff=False)[0]

        cls.client = APIClient()

    def test_should_not_accept_non_admin_user(self):
        token, _ = Token.objects.get_or_create(user_id=self.user.id)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        try:
            response = self.client.delete(f"/api/events/{self.event.id}/")
        except Exception as e:
            self.fail(f"deletion is failing with message: {str(e)}")

        response_dict = response.json()

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertIn("detail", response_dict.keys())

    def test_should_not_accept_invalid_token(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token 1234")

        try:
            response = self.client.delete(f"/api/events/{self.event.id}/")
        except Exception as e:
            self.fail(f"deletion is failing with message: {str(e)}")

        response_dict = response.json()

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn("detail", response_dict.keys())

    def test_should_delete_event(self):
        token, _ = Token.objects.get_or_create(user_id=self.admin_user.id)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        try:
            response = self.client.delete(f"/api/events/{self.event.id}/")
        except Exception as e:
            self.fail(f"deletion is failing with message: {str(e)}")

        try:
            Event.objects.get(id=self.event.id)
        except:
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
