import uuid

from events.models import Event
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status
from reviews.models import Review
from users.models import User


class CreateReviewTest(APITestCase):
    fixtures = [
        "user-fixture.json",
        "event-fixture.json",
        "address-fixture.json",
        "category-fixture.json",
        "review-fixture.json",
    ]

    @classmethod
    def setUpTestData(cls):
        cls.event = Event.objects.all()[0]
        cls.user = User.objects.all()[0]

        cls.review_data = {
            "title": "Show da Daniela Mercury",
            "description": "Daniela faz seu primeiro show em...",
            "rating": 5,
        }

        cls.client = APIClient()

    def test_should_create_review(self):
        token, _ = Token.objects.get_or_create(user_id=self.user.id)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        response = self.client.post(
            f"/api/events/{self.event.id}/reviews/", self.review_data
        )
        response_dict = response.json()
        review = Review.objects.get(id=response_dict["id"])

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(uuid.UUID(response_dict["id"]))

        self.assertEqual(response_dict["title"], self.review_data["title"])
        self.assertEqual(response_dict["description"], self.review_data["description"])
        self.assertEqual(response_dict["rating"], self.review_data["rating"])

        self.assertEqual(response_dict["title"], review.title)
        self.assertEqual(response_dict["description"], review.description)
        self.assertEqual(response_dict["rating"], review.rating)

    def test_should_not_create_review_without_data(self):
        token, _ = Token.objects.get_or_create(user_id=self.user.id)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        response = self.client.post(f"/api/events/{self.event.id}/reviews/", {})
        response_dict = response.json()

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertIn("title", response_dict.keys())
        self.assertIn("description", response_dict.keys())
        self.assertIn("rating", response_dict.keys())

    def test_should_not_create_review_without_token(self):
        response = self.client.post(
            f"/api/events/{self.event.id}/reviews/", self.review_data
        )
        response_dict = response.json()

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.assertIn("detail", response_dict.keys())
