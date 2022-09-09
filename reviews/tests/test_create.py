import uuid
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from rest_framework.authtoken.models import Token

from users.models import User
from events.models import Event
from reviews.models import Review

class CreateReviewTest(APITestCase):
    fixtures = ['user-fixture.json', 'event-fixture.json']

    @classmethod
    def setUpTestData(cls):
        cls.event      = Event.objects.all()[0]
        cls.user       = User.objects.all()[0]

        cls.review_data = {
            "title":"Show da Daniela Mercury",
            "description":"Daniela faz seu primeiro show em...",
            "rating":10,
        }

        cls.client = APIClient()
    
    def test_should_create_review(self):
        token,_ = Token.objects.get_or_create(user_id=self.user.id)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        response      = self.client.post(f'/api/events/{self.event.id}/reviews/', self.review_data)
        response_dict = response.json()
        review        = Review.objects.get(id=response_dict["id"])

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(uuid.UUID(response_dict["id"]))

        self.assertEqual(response_dict["title"], self.review_data["title"])
        self.assertEqual(response_dict["description"], self.review_data["description"])
        self.assertEqual(response_dict["rating"], self.review_data["rating"])

        self.assertEqual(response_dict["title"], review.title)
        self.assertEqual(response_dict["hour"], review.hour)
        self.assertEqual(response_dict["description"], review.description)
        self.assertEqual(response_dict["rating"], review.rating)

    def test_should_not_create_review_without_data(self):
        token,_ = Token.objects.get_or_create(user_id=self.user.id)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        response      = self.client.post(f'/api/events/{self.event.id}/reviews/', {})
        response_dict = response.json()

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertIn("title", response_dict.keys())
        self.assertIn("description", response_dict.keys())
        self.assertIn("rating", response_dict.keys())
    
    def test_should_not_create_review_without_token(self):
        response      = self.client.post(f'/api/events/{self.event.id}/reviews/', self.review_data)
        response_dict = response.json()

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.assertIn("detail", response_dict.keys())