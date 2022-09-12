import uuid

from django.contrib.auth.hashers import check_password
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status
from users.models import User


class RegisterTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_data = {
            "username": "raniery",
            "email": "rani@kenzie.com",
            "password": "1234",
            "first_name": "raniery",
            "last_name": "almeida",
            "is_promoter": False,
        }

        cls.promoter_data = {
            "username": "bateman",
            "password": "1234",
            "email": "bateman@bateman.com",
            "first_name": "patrick",
            "last_name": "bateman",
            "is_promoter": True,
        }

        cls.client = APIClient()

    def test_should_create_user(self):
        try:
            response = self.client.post("/api/register/", self.user_data)
        except Exception as e:
            self.fail(f"Creation failed with error:{str(e)}")

        response_dict = response.json()
        user = User.objects.get(id=response_dict["id"])

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(uuid.UUID(response_dict["id"]))

        self.assertEqual(response_dict["username"], self.user_data["username"])
        self.assertEqual(response_dict["first_name"], self.user_data["first_name"])
        self.assertEqual(response_dict["email"], self.user_data["email"])
        self.assertEqual(response_dict["last_name"], self.user_data["last_name"])
        self.assertEqual(response_dict["is_promoter"], self.user_data["is_promoter"])

        self.assertEqual(response_dict["username"], user.username)
        self.assertEqual(response_dict["first_name"], user.first_name)
        self.assertEqual(response_dict["email"], user.email)
        self.assertEqual(response_dict["last_name"], user.last_name)
        self.assertEqual(response_dict["is_promoter"], user.is_promoter)

        self.assertTrue(check_password(self.user_data["password"], user.password))

    def test_should_create_promoter(self):
        try:
            response = self.client.post("/api/register/", self.promoter_data)
        except Exception as e:
            self.fail(f"Creation failed with error:{str(e)}")

        response_dict = response.json()
        user = User.objects.get(id=response_dict["id"])

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(uuid.UUID(response_dict["id"]))

        self.assertEqual(response_dict["username"], self.promoter_data["username"])
        self.assertEqual(response_dict["first_name"], self.promoter_data["first_name"])
        self.assertEqual(response_dict["email"], self.promoter_data["email"])
        self.assertEqual(response_dict["last_name"], self.promoter_data["last_name"])
        self.assertEqual(
            response_dict["is_promoter"], self.promoter_data["is_promoter"]
        )

        self.assertEqual(response_dict["username"], user.username)
        self.assertEqual(response_dict["first_name"], user.first_name)
        self.assertEqual(response_dict["email"], user.email)
        self.assertEqual(response_dict["last_name"], user.last_name)
        self.assertEqual(response_dict["is_promoter"], user.is_promoter)

        self.assertTrue(check_password(self.promoter_data["password"], user.password))

    def test_should_not_create_user_without_data(self):
        response = self.client.post("/api/register/", {})
        response_dict = response.json()

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertIn("username", response_dict.keys())
        self.assertIn("password", response_dict.keys())
        self.assertIn("first_name", response_dict.keys())
        self.assertIn("last_name", response_dict.keys())
