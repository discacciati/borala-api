from rest_framework.test import APITestCase
from events.models import Event
from line_up.models import LineUp
from line_up.serializers import LineUpSerializer

class LineupRelationTest(APITestCase):
    fixtures = ['lineup-fixture.json', 'event-fixture.json']

    @classmethod
    def setUpTestData(cls) -> None:
        cls.new_lineup_data = {
            "title":"Show da Daniela Mercury",
            "hour":"19:00",
            "description":"Daniela faz seu primeiro show em...",
            "talent":"Daniela Mercury",
        }

        cls.lineup_serializer = LineUpSerializer(data=cls.new_lineup_data)
        cls.lineup            = LineUp.objects.all()[0]
    
    def should_not_create_lineup_without_event(self):
        try:
            self.lineup_serializer.is_valid(raise_exception=True)
            self.lineup_serializer.save()
            self.fail("lineup being saved without event")
        except:
            self.assertEqual(len(LineUp.objects.filter(**self.new_lineup_data)), 0)
    
    def test_lineup_should_have_correct_event(self):
        lineup_event = self.lineup.event
        db_event     = Event.objects.get(id=lineup_event.id)

        self.assertEqual(self.lineup.id, db_event.event.id)

        self.assertEqual(lineup_event.name, db_event.name)
        self.assertEqual(lineup_event.description, db_event.description)
        self.assertEqual(lineup_event.date, db_event.date)