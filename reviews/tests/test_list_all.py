from events.models import Event
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status
from reviews.models import Review


class ReviewListTest(APITestCase):
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
        cls.reviews_list = Review.objects.filter(event_id=cls.event.id)
        cls.reviews_len = len(cls.reviews_list)

        cls.client = APIClient()

    def test_should_list_all_reviews(self):
        response = self.client.get(f"/api/events/{self.event.id}/reviews/")
        response_list = response.json()["results"]
        response_dict = {
            response_list[i]["id"]: resp for i, resp in enumerate(response_list)
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_list), self.reviews_len)

        for review in self.reviews_list:
            id_string = str(review.id)
            response_data = response_dict[id_string]

            self.assertEqual(response_data["title"], review.title)
            self.assertEqual(response_data["description"], review.description)
            self.assertEqual(response_data["rating"], review.rating)
