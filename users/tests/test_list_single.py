from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status
from users.models import User


class UserListOneTest(APITestCase):
    fixtures = ["user-fixture.json"]

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.all()[1]
        cls.admin = User.objects.filter(is_superuser=True)[0]

        cls.client = APIClient()

    def test_should_list_user_as_user(self):
        token, _ = Token.objects.get_or_create(user_id=self.user.id)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        response = self.client.get(f"/api/users/{self.user.id}/")
        response_dict = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response_dict["id"], str(self.user.id))
        self.assertEqual(response_dict["username"], self.user.username)
        self.assertEqual(response_dict["email"], self.user.email)
        self.assertEqual(response_dict["first_name"], self.user.first_name)
        self.assertEqual(response_dict["last_name"], self.user.last_name)
        self.assertEqual(response_dict["is_promoter"], self.user.is_promoter)

    def test_should_list_user_as_admin(self):
        token, _ = Token.objects.get_or_create(user_id=self.admin.id)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        response = self.client.get(f"/api/users/{self.user.id}/")
        response_dict = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response_dict["id"], str(self.user.id))
        self.assertEqual(response_dict["username"], self.user.username)
        self.assertEqual(response_dict["email"], self.user.email)
        self.assertEqual(response_dict["first_name"], self.user.first_name)
        self.assertEqual(response_dict["last_name"], self.user.last_name)
        self.assertEqual(response_dict["is_promoter"], self.user.is_promoter)
