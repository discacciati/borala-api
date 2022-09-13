from events.models import Event
from line_up.models import LineUp
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status
from users.models import User


class LineupPatchTest(APITestCase):
    fixtures = [
        "user-fixture.json",
        "event-fixture.json",
        "address-fixture.json",
        "category-fixture.json",
        "lineup-fixture.json",
    ]

    @classmethod
    def setUpTestData(cls):
        event = Event.objects.all()[2]
        lineup_list = LineUp.objects.filter(event_id=event.id)

        cls.event = event
        cls.lineup = lineup_list[0]
        cls.second_lineup = lineup_list[1]
        cls.owner = User.objects.get(id=cls.event.user.id)
        cls.other_user = User.objects.filter(is_promoter=False)[0]

        cls.lineup_patch_info = {
            "title": "Show do Luan Santana",
            "is_active": False,
        }

        cls.previous_data = {
            "title": cls.lineup.title,
            "is_active": cls.lineup.is_active,
        }

        cls.client = APIClient()

    def test_should_not_accept_other_user(self):
        token, _ = Token.objects.get_or_create(user_id=self.other_user.id)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        try:
            response = self.client.patch(
                f"/api/events/{self.event.id}/lineup/{self.lineup.id}/"
            )
        except Exception as e:
            self.fail(f"deletion is failing with message: {str(e)}")

        response_dict = response.json()

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertIn("detail", response_dict.keys())

        try:
            database_lineup = LineUp.objects.get(id=self.lineup.id)
        except:
            self.fail("Patch should not delete object")

        self.assertNotEqual(database_lineup.title, self.lineup_patch_info["title"])
        self.assertNotEqual(
            database_lineup.is_active, self.lineup_patch_info["is_active"]
        )

    def test_should_not_accept_invalid_token(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token 1234")

        try:
            response = self.client.patch(
                f"/api/events/{self.event.id}/lineup/{self.lineup.id}/"
            )
        except Exception as e:
            self.fail(f"Patch is failing with message: {str(e)}")

        response_dict = response.json()

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn("detail", response_dict.keys())

    def test_should_update_lineup(self):
        token, _ = Token.objects.get_or_create(user_id=self.owner.id)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        try:
            response = self.client.patch(
                f"/api/events/{self.event.id}/lineup/{self.lineup.id}/",
                self.lineup_patch_info
            )
        except Exception as e:
            self.fail(f"Patch is failing with message: {str(e)}")

        response_dict = response.json()
        print(response_dict)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        try:
            database_lineup = LineUp.objects.get(id=self.lineup.id)
        except:
            self.fail("Patch should not delete object")

        self.assertEqual(response_dict["title"], self.lineup_patch_info["title"])
        self.assertEqual(
            response_dict["is_active"], self.lineup_patch_info["is_active"]
        )

        self.assertEqual(database_lineup.title, self.lineup_patch_info["title"])
        self.assertEqual(
            database_lineup.is_active, self.lineup_patch_info["is_active"]
        )
