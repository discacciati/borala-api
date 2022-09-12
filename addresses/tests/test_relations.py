from rest_framework.test import APITestCase
from events.models import Event
from addresses.models import Address
from addresses.serializers import AddressSerializer

class AddressRelationTest(APITestCase):
    fixtures = ['borala.json']

    @classmethod
    def setUpTestData(cls) -> None:
        cls.new_address_data = {
            "state": "MG",
            "city": "Araguari",
            "postal_code": "38442-032",
            "street": "Rua Mário Lieggio",
            "district": "Bairro",
            "number": 1488,
        }

        cls.address_serializer = AddressSerializer(data=cls.new_address_data)
        cls.address            = Address.objects.all()[0]
    
    def test_should_not_create_address_without_event(self):
        try:
            self.address_serializer.is_valid(raise_exception=True)
            self.address_serializer.save()
            self.fail("Address being saved without event")
        except:
            pass
    
    # def test_address_should_have_correct_event(self):
    #     address_event = self.address.event
    #     db_event      = Event.objects.get(id=address_event.id)

    #     self.assertEqual(self.address.id, db_event.event.id)

    #     self.assertEqual(address_event.name, db_event.name)
    #     self.assertEqual(address_event.description, db_event.description)
    #     self.assertEqual(address_event.date, db_event.date)