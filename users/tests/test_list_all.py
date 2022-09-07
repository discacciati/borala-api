from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status

from users.models import User

class UserListTest(APITestCase):
    fixtures = ["user-fixture.json"]

    @classmethod
    def setUpTestData(cls):
        cls.users_list = User.objects.all()
        cls.users_len  = len(cls.users_list)

        cls.client = APIClient()
    
    def test_should_list_all_users(self):
        response      = self.client.get("/api/users/")
        response_list = response.json()
        response_dict = {response_list[i]["id"]:resp for i,resp in enumerate(response_list)}

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_list), self.users_len)

        for user in self.users_list:
            id_string     = str(user.id)
            response_data = response_dict[id_string]

            self.assertEqual(response_data["id"], id_string)
            self.assertEqual(response_data["username"], user.username)
            self.assertEqual(response_data["email"], user.email)
            self.assertEqual(response_data["first_name"], user.first_name)
            self.assertEqual(response_data["last_name"], user.last_name)
            self.assertEqual(response_data["is_promoter"], user.is_promoter)