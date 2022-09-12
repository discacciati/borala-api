from uuid import UUID

from addresses.models import Address
from django.db.utils import IntegrityError
from django.test import TestCase


class ModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.address_data = {
            "state": "MG",
            "city": "Araguari",
            "postal_code": "38442-032",
            "street": "Rua Mário Lieggio",
            "district": "Bairro",
            "number": 1488,
        }

        cls.address = Address(**cls.address_data)

        cls.address_keys = [
            "id",
            "state",
            "city",
            "postal_code",
            "street",
            "district",
            "number",
        ]

    def test_should_return_keys(self):
        for key in self.address_data:
            self.assertIn(key, self.address.__dict__)

    def test_should_return_expected_values(self):
        self.assertEqual(self.address.state, self.address_data["state"])
        self.assertEqual(self.address.city, self.address_data["city"])
        self.assertEqual(self.address.postal_code, self.address_data["postal_code"])
        self.assertEqual(self.address.street, self.address_data["street"])
        self.assertEqual(self.address.district, self.address_data["district"])
        self.assertEqual(self.address.number, self.address_data["number"])
        self.assertTrue(UUID(str(self.address.id)))

    def test_fields_should_have_max_length(self):
        state_max_length = self.address._meta.get_field("state").max_length
        city_max_length = self.address._meta.get_field("city").max_length
        postal_code_max_length = self.address._meta.get_field("postal_code").max_length
        street_max_length = self.address._meta.get_field("street").max_length
        district_max_length = self.address._meta.get_field("district").max_length

        self.assertEqual(state_max_length, 2)
        self.assertEqual(city_max_length, 50)
        self.assertEqual(postal_code_max_length, 10)
        self.assertEqual(street_max_length, 50)
        self.assertEqual(district_max_length, 50)

    def test_number_should_be_valid(self):
        invalid_number_data = {**self.address_data}
        invalid_number_data["number"] = -4

        with self.assertRaises(IntegrityError):
            Address.objects.create(**invalid_number_data)
