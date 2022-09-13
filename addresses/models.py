import uuid

from django.db import models


class Address(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    state = models.CharField(max_length=2)
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    street = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    number = models.PositiveIntegerField(null=True, blank=True)

    def __repr__(self) -> str:
        return f"Adress({self.street} n°{self.number}, {self.city}-{self.state})"
