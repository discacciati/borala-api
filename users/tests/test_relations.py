from rest_framework.test import APITestCase
from users.models import User
from events.models import Event
from reviews.models import Review

class UserRelationTest(APITestCase):
    fixtures = ['borala.json']

    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = User.objects.filter(is_promoter=True)[0]
    
    def test_user_should_have_correct_events(self):
        user_events = self.user.events.all()

        for event in user_events:
            db_event = Event.objects.get(id=event.id)

            self.assertEqual(event.id, db_event.id)

            self.assertEqual(event.title, db_event.title)
            self.assertEqual(event.description, db_event.description)
            self.assertEqual(event.date, db_event.date)


    def test_user_should_have_correct_reviews(self):
        user_reviews = self.user.reviews.all()

        for review in user_reviews:
            db_review = Review.objects.get(id=review.id)

            self.assertEqual(review.id, db_review.id)

            self.assertEqual(review.title, db_review.title)
            self.assertEqual(review.description, db_review.description)
            self.assertEqual(review.rating, db_review.rating)
