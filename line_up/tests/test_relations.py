from events.models import Event
from line_up.models import LineUp
from line_up.serializers import LineupSerializer
from rest_framework.test import APITestCase


class LineupRelationTest(APITestCase):
    fixtures = ["borala.json"]

    @classmethod
    def setUpTestData(cls) -> None:
        cls.new_lineup_data = {
            "title": "Show da Daniela Mercury",
            "hour": "19:00",
            "description": "Daniela faz seu primeiro show em...",
            "talent": "Daniela Mercury",
        }

        cls.lineup_serializer = LineupSerializer(data=cls.new_lineup_data)
        cls.lineup = LineUp.objects.all()[0]

    def test_should_not_create_lineup_without_event(self):
        try:
            self.lineup_serializer.is_valid(raise_exception=True)
            self.lineup_serializer.save()
            self.fail("lineup being saved without event")
        except:
            pass

    def test_lineup_should_have_correct_event(self):
        lineup_event = self.lineup.event
        db_event = Event.objects.get(id=lineup_event.id)

        self.assertEqual(lineup_event.id, db_event.id)

        self.assertEqual(lineup_event.title, db_event.title)
        self.assertEqual(lineup_event.description, db_event.description)
        self.assertEqual(lineup_event.date, db_event.date)
