from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from rest_framework.authtoken.models import Token

from users.models import User
from events.models import Event
from reviews.models import Review

class EventPatchTest(APITestCase):
    fixtures = [
        'user-fixture.json',
        'event-fixture.json', 
        'address-fixture.json', 
        'category-fixture.json', 
        'review-fixture.json'
    ]

    @classmethod
    def setUpTestData(cls):
        event       = Event.objects.all()[0]
        review_list = Review.objects.filter(event_id=event.id)
        
        cls.event         = event
        cls.review        = review_list[0]
        cls.second_review = review_list[1]
        cls.owner         = User.objects.get(id=cls.review.user.id)
        cls.other_user    = User.objects.all().exclude(id=cls.review.user.id,)[0]

        cls.review_patch_info = {
            "title":"Show do Luan Santana",
            "rating":3,
        }

        cls.previous_data = {
            "title": cls.review.title,
            "rating": cls.review.rating
        }

        cls.client = APIClient()
    
    def test_should_not_accept_other_user(self):
        token,_ = Token.objects.get_or_create(user_id=self.other_user.id)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        response      = self.client.patch(f"/api/events/{self.event.id}/reviews/{self.second_review.id}/", self.review_patch_info)
        response_dict = response.json()

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)        
        self.assertIn('detail', response_dict.keys())

        try:
            database_review = Review.objects.get(id=self.second_review.id)
        except:
            self.fail("Patch should not delete object")

        self.assertNotEqual(database_review.title, self.review_patch_info["title"])
        self.assertNotEqual(database_review.rating, self.review_patch_info["rating"])

    def test_should_not_accept_invalid_token(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token 1234')

        response      = self.client.patch(f"/api/events/{self.event.id}/reviews/{self.second_review.id}/", self.review_patch_info)
        response_dict = response.json()

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)        
        self.assertIn('detail', response_dict.keys())

        try:
            database_review = Review.objects.get(id=self.second_review.id)
        except:
            self.fail("Patch should not delete object")

        self.assertNotEqual(database_review.title, self.review_patch_info["title"])
        self.assertNotEqual(database_review.rating, self.review_patch_info["rating"])
    
    def test_should_update_review(self):
        token,_ = Token.objects.get_or_create(user_id=self.owner.id)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        response      = self.client.patch(f"/api/events/{self.event.id}/reviews/{self.review.id}/", self.review_patch_info)
        response_dict = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)        

        try:
            database_review = Review.objects.get(id=self.review.id)
        except:
            self.fail("Patch should not delete object")

        self.assertEqual(response_dict["title"], self.review_patch_info["title"])
        self.assertEqual(response_dict["rating"], self.review_patch_info["rating"])

        self.assertEqual(database_review.title, self.review_patch_info["title"])
        self.assertEqual(database_review.rating, self.review_patch_info["rating"])
