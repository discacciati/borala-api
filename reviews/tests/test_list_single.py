from events.models import Event
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status
from reviews.models import Review


class ReviewListOneTest(APITestCase):
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
        cls.review = Review.objects.filter(event_id=cls.event.id)[0]

        cls.client = APIClient()

    def test_should_list_single_review(self):
        response = self.client.get(
            f"/api/events/{self.event.id}/reviews/{self.review.id}/"
        )
        response_dict = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response_dict["title"], self.review.title)
        self.assertEqual(response_dict["description"], self.review.description)
        self.assertEqual(response_dict["rating"], self.review.rating)
