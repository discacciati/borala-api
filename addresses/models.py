import uuid

from django.db import models


class Address(models.Model):
    id = models.UUIDField(default=uuid.uuid4(), primary_key=True, editable=False)
    state = models.CharField(max_length=2)
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10, blank=True)
    street = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    number = models.PositiveIntegerField()

    def __repr__(self) -> str:
        return f"Adress({self.street} n°{self.number}, {self.city}-{self.state})"
