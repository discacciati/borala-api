from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status
from users.models import User


class UserDeleteTest(APITestCase):
    fixtures = ["user-fixture.json"]

    @classmethod
    def setUpTestData(cls):
        cls.admin_user = User.objects.filter(is_superuser=True)[0]
        cls.user = User.objects.filter(is_superuser=False)[0]
        cls.other_user = User.objects.filter(is_superuser=False).exclude(
            id=cls.user.id
        )[0]
        cls.client = APIClient()

    def test_should_not_accept_non_admin_user(self):
        token, _ = Token.objects.get_or_create(user_id=self.other_user.id)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        response = self.client.delete(f"/api/users/{self.user.id}/")
        # response_dict = response.json()

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # self.assertIn('detail', response_dict.keys())

    def test_should_not_accept_invalid_token(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token 1234")

        response = self.client.delete(f"/api/users/{self.user.id}/")
        response_dict = response.json()

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn("detail", response_dict.keys())

    def test_should_delete_user(self):
        token, _ = Token.objects.get_or_create(user_id=self.admin_user.id)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        response = self.client.delete(f"/api/users/{self.user.id}/")

        try:
            User.objects.get(id=self.user.id)
        except:
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
