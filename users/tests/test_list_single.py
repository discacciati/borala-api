from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status

from users.models import User

class UserListOneTest(APITestCase):
    fixtures = ["user-fixture.json"]

    @classmethod
    def setUpTestData(cls):
        cls.user  = User.objects.all()[0]

        cls.client = APIClient()
    
    def test_should_list_user(self):
        response      = self.client.get("/api/users/")
        response_dict = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response_dict["id"], str(self.user.id))
        self.assertEqual(response_dict["username"], self.user.username)
        self.assertEqual(response_dict["email"], self.user.email)
        self.assertEqual(response_dict["first_name"], self.user.first_name)
        self.assertEqual(response_dict["last_name"], self.user.last_name)
        self.assertEqual(response_dict["is_promoter"], self.user.is_promoter)