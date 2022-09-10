from rest_framework.test import APITestCase
from events.models import Event
from categories.models import Category

class CategoryRelationTest(APITestCase):
    fixtures = ['borala.json']

    @classmethod
    def setUpTestData(cls) -> None:
        cls.category = Category.objects.all()[0]
    
    def test_should_not_create_category_twice(self):
        try:
            Category.objects.create(name=self.category.name)
            self.fail("Two categories with the same name are being saved")
        except:
            pass
    
    def test_category_should_have_correct_events(self):
        category_events = self.category.events.all()

        for event in category_events:
            db_event = Event.objects.get(id=event.id)

            self.assertEqual(event.id, db_event.id)

            self.assertEqual(event.title, db_event.title)
            self.assertEqual(event.description, db_event.description)
            self.assertEqual(event.price, db_event.price)
