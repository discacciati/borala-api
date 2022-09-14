from rest_framework.test import APITestCase

from users.models import User
from events.models import Event
from events.serializers import EventSerializer
from reviews.models import Review
from line_up.models import LineUp

class EventRelationsTest(APITestCase):
    fixtures = ['borala.json']

    @classmethod
    def setUpTestData(cls) -> None:
        cls.promoter = User.objects.filter(is_promoter=True)[0]

        cls.new_event_data = {
            "title":"festa no ape",
            "date":"2022-09-07",
            "description":"vai rolar bunda-lele",
            "categories":[{"name":"festa"}, {"name": "ape"}],
            "address":{
                "state": "MG",
                "city": "Araguari",
                "postal_code": "38442-032",
                "street": "Rua Mário Lieggio",
                "district": "Bairro",
                "number": 1488,
            }
        }

        cls.event_serializer = EventSerializer(data=cls.new_event_data)
        cls.event            = Event.objects.all()[0]

    def test_should_not_create_event_without_promoter(self):
        try:
            self.event_serializer.is_valid(raise_exception=True)
            self.event_serializer.save()
            self.fail("event being saved without user")
        except:
            pass

    def test_categories_should_be_created_with_event(self):
        try:
            self.event_serializer.is_valid(raise_exception=True)
            new_event       = self.event_serializer.save(user=self.promoter)
        except Exception as e:
            self.fail(f'Failed creating event with error: {str(e)}')
        
        categories      = new_event.categories.all()
        categories_data = self.new_event_data["categories"]

        for category_data in categories_data:
            matches = [c for c in categories if c.name == category_data["name"]]

            self.assertEqual(len(matches), 1)
    
    def test_address_should_be_created_with_event(self):
        try:
            self.event_serializer.is_valid(raise_exception=True)
            new_event       = self.event_serializer.save(user=self.promoter)
        except Exception as e:
            self.fail(f'Failed creating event with error: {str(e)}')

        address      = new_event.address
        address_data = self.new_event_data["address"]

        self.assertEqual(address.state, address_data["state"])
        self.assertEqual(address.city, address_data["city"])
        self.assertEqual(address.postal_code, address_data["postal_code"])
        self.assertEqual(address.street, address_data["street"])
        self.assertEqual(address.district, address_data["district"])
        self.assertEqual(address.number, address_data["number"])
    
    def test_event_should_have_correct_reviews(self):
        event_reviews = self.event.reviews.all()

        for review in event_reviews:
            db_review = Review.objects.get(id=review.id)

            self.assertEqual(self.event.id, db_review.event.id)

            self.assertEqual(review.title, db_review.title)
            self.assertEqual(review.description, db_review.description)
            self.assertEqual(review.rating, db_review.rating)
    
    def test_event_should_have_correct_lineup(self):
        event_lineup = self.event.lineup.all()

        for lineup in event_lineup:
            db_lineup = LineUp.objects.get(id=lineup.id)

            self.assertEqual(self.event.id, db_lineup.event.id)

            self.assertEqual(lineup.title, db_lineup.title)
            self.assertEqual(lineup.description, db_lineup.description)
            self.assertEqual(lineup.rating, db_lineup.rating)
            self.assertEqual(lineup.hour, db_lineup.hour)
            self.assertEqual(lineup.price, db_lineup.price)
            self.assertEqual(lineup.talent, db_lineup.talent)
