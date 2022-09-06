from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from rest_framework.authtoken.models import Token

from users.models import User

class UserPatchTest(APITestCase):
    fixtures = ["user-fixture.json"]

    @classmethod
    def setUpTestData(cls):
        user_list = User.objects.all()

        cls.user       = user_list[0]
        cls.other_user = user_list[1]

        cls.user_patch_info = {
            "last_name":"Oliveira",
            "is_active":False,
        }

        cls.client = APIClient()
    
    def test_should_update_user(self):
        token,_ = Token.objects.get_or_create(user_id=self.user.id)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        response      = self.client.patch(f"/api/users/{self.user.id}/", self.user_patch_info)
        response_dict = response.json()
        updated_user  = User.objects.get(id=response_dict["id"])

        self.assertEqual(response.status_code, status.HTTP_200_OK)        
        self.assertEqual(response_dict["last_name"], self.user_patch_info["last_name"])
        self.assertEqual(response_dict["last_name"], updated_user.last_name)
        
    def test_should_not_accept_other_user(self):
        token,_ = Token.objects.get_or_create(user_id=self.other_user.id)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        response      = self.client.patch(f"/api/users/{self.user.id}/", self.user_patch_info)
        response_dict = response.json()

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)        
        self.assertIn('detail', response_dict.keys())

    def test_should_not_accept_invalid_token(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token 1234')

        response      = self.client.patch(f"/api/users/{self.user.id}/", self.user_patch_info)
        response_dict = response.json()

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)        
        self.assertIn('detail', response_dict.keys())
