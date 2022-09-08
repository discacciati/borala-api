from rest_framework.test import APITestCase
from events.models import Event
from reviews.models import Review
from users.models   import User
from reviews.serializers import ReviewSerializer

class ReviewRelationTest(APITestCase):
    fixtures = ['review-fixture.json', 'event-fixture.json']

    @classmethod
    def setUpTestData(cls) -> None:
        cls.new_review_data = {
            "title":"Show da Daniela Mercury",
            "description":"Daniela faz seu primeiro show em...",
            "rating":10,
        }

        cls.review_serializer = ReviewSerializer(data=cls.new_review_data)
        cls.review            = Review.objects.all()[0]
    
    def should_not_create_review_without_user_or_event(self):
        try:
            self.review_serializer.is_valid(raise_exception=True)
            self.review_serializer.save()
            self.fail("review being saved without event or user")
        except:
            self.assertEqual(len(Review.objects.filter(**self.new_review_data)), 0)
    
    def test_review_should_have_correct_event(self):
        review_event = self.review.event
        db_event     = Event.objects.get(id=review_event.id)

        self.assertEqual(self.review.id, db_event.event.id)

        self.assertEqual(review_event.name, db_event.name)
        self.assertEqual(review_event.description, db_event.description)
        self.assertEqual(review_event.date, db_event.date)

    def test_review_should_have_correct_user(self):
        review_user = self.review.user
        db_user     = User.objects.get(id=review_user.id)

        self.assertEqual(self.review.id, db_user.review.id)

        self.assertEqual(review_user.username, db_user.first_name)
        self.assertEqual(review_user.first_name, db_user.first_name)
        self.assertEqual(review_user.last_name, db_user.last_name)
        self.assertEqual(review_user.email, db_user.email)
        self.assertEqual(review_user.is_promoter, db_user.is_promoter)