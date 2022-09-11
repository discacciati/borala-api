from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from rest_framework.authtoken.models import Token

class LoginTest(APITestCase):
    fixtures = ['user-fixture.json']
    
    @classmethod
    def setUpTestData(cls):
        cls.promoter_login_credentials = {
            "username":"promoter",
            "password":"1234",
        }

        cls.user_login_credentials = {
            "username":"comum",
            "password":"1234",
        }

        cls.client = APIClient()

    
    def test_should_login_user(self):
        response       = self.client.post("/api/login/", self.user_login_credentials)
        response_dict  = response.json()
        response_token = response_dict["token"]
        user_token     = Token.objects.get(user__username=self.user_login_credentials["username"])

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertIn("token", response_dict.keys())
        self.assertEqual(response_token, user_token.key)

    def test_should_login_promoter(self):
        response       = self.client.post("/api/login/", self.promoter_login_credentials)
        response_dict  = response.json()
        response_token = response_dict["token"]
        user_token     = Token.objects.get(user__username=self.promoter_login_credentials["username"])

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertIn("token", response_dict.keys())
        self.assertEqual(response_token, user_token.key)
    
    def test_should_block_invalid_credentials(self):
        response      = self.client.post("/api/login/", {})
        response_dict = response.json()

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertIn("username", response_dict.keys())
        self.assertIn("password", response_dict.keys())
