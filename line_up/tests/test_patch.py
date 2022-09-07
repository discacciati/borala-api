from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from rest_framework.authtoken.models import Token

from users.models import User
from events.models import Event
from line_up.models import Lineup

class EventPatchTest(APITestCase):
    fixtures = ["user-fixture.json", "event-fixture.json", "lineup-fixture.json"]

    @classmethod
    def setUpTestData(cls):
        event       = Event.objects.all()[0]
        lineup_list = Lineup.objects.filter(event_id=event.id)
        
        cls.event         = event
        cls.lineup        = lineup_list[0]
        cls.second_lineup = lineup_list[1]
        cls.owner         = User.objects.get(id=cls.event.user.id)
        cls.other_user    = User.objects.get(is_promoter=False)

        cls.lineup_patch_info = {
            "title":"Show do Luan Santana",
            "is_active":False,
        }

        cls.previous_data = {
            "name": cls.lineup.name,
            "is_active": cls.lineup.is_active
        }

        cls.client = APIClient()
    
    def test_should_not_accept_other_user(self):
        token,_ = Token.objects.get_or_create(user_id=self.other_user.id)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        response      = self.client.patch(f"/api/events/{self.event.id}/lineup/{self.second_lineup.id}/", self.lineup_patch_info)
        response_dict = response.json()

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)        
        self.assertIn('detail', response_dict.keys())

        try:
            database_lineup = Lineup.objects.get(self.second_lineup.id)
        except:
            self.fail("Patch should not delete object")

        self.assertNotEqual(database_lineup.name, self.lineup_patch_info["name"])
        self.assertNotEqual(database_lineup.is_active, self.lineup_patch_info["is_active"])

    def test_should_not_accept_invalid_token(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token 1234')

        response      = self.client.patch(f"/api/events/{self.event.id}/lineup/{self.second_lineup.id}/", self.lineup_patch_info)
        response_dict = response.json()

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)        
        self.assertIn('detail', response_dict.keys())
    
    def test_should_update_lineup(self):
        token,_ = Token.objects.get_or_create(user_id=self.owner.id)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        response      = self.client.patch(f"/api/events/{self.event.id}/lineup/{self.lineup.id}/", self.lineup_patch_info)
        response_dict = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)        

        try:
            database_event = Event.objects.get(self.second_lineup.id)

            self.assertEqual(response_dict["title"], self.lineup_patch_info["title"])
            self.assertEqual(response_dict["is_active"], self.lineup_patch_info["is_active"])

            self.assertEqual(database_event.title, self.lineup_patch_info["title"])
            self.assertEqual(database_event.is_active, self.lineup_patch_info["is_active"])
        except:
            self.fail("Patch should not delete object")
