from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from rest_framework.authtoken.models import Token

from users.models import User
from events.models import Event


class EventPatchTest(APITestCase):
    fixtures = ["user-fixture.json", "event-fixture.json", "address-fixture.json", "category-fixture.json"]

    @classmethod
    def setUpTestData(cls):
        

        cls.event        = Event.objects.all()[0]
        cls.second_event = Event.objects.all()[1]
        cls.owner        = User.objects.get(id=cls.event.user.id)
        cls.other_user   = User.objects.filter(is_promoter=False)[0]

        cls.event_patch_info = {
            "title":"Farra da boa",
            "is_active":False,
        }

        cls.previous_data = {
            "title": cls.event.title,
            "is_active": cls.event.is_active
        }

        cls.client = APIClient()
    
    def test_should_not_accept_other_user(self):
        token,_ = Token.objects.get_or_create(user_id=self.other_user.id)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        response      = self.client.patch(f"/api/events/{self.second_event.id}/", self.event_patch_info)
        response_dict = response.json()

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)        
        self.assertIn('detail', response_dict.keys())

        try:
            database_event = Event.objects.get(id=self.second_event.id)
        except:
            self.fail("Patch should not delete object")

        self.assertNotEqual(database_event.title, self.event_patch_info["title"])
        self.assertNotEqual(database_event.is_active, self.event_patch_info["is_active"])

    def test_should_not_accept_invalid_token(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token 1234')

        response      = self.client.patch(f"/api/events/{self.event.id}/", self.event_patch_info)
        response_dict = response.json()

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)        
        self.assertIn('detail', response_dict.keys())
    
    def test_should_update_event(self):
        token,_ = Token.objects.get_or_create(user_id=self.owner.id)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        response      = self.client.patch(f"/api/events/{self.event.id}/", self.event_patch_info)
        response_dict = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)        

        try:
            database_event = Event.objects.get(id=self.event.id)
        except:
            self.fail("Patch should not delete object")

        self.assertEqual(response_dict["title"], self.event_patch_info["title"])
        self.assertEqual(response_dict["is_active"], self.event_patch_info["is_active"])

        self.assertEqual(database_event.title, self.event_patch_info["title"])
        self.assertEqual(database_event.is_active, self.event_patch_info["is_active"])
