import uuid

from django.db import models


class Event(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField(null=True, blank=True)
    image_url = models.TextField(null=True)
    site_url = models.TextField(null=True)
    price = models.FloatField(null=True, blank=True, default=0)
    sponsor = models.CharField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(blank=True, null=True, default=True)

    categories = models.ManyToManyField("categories.Category", related_name="events")
    user = models.ForeignKey(
        "users.user", on_delete=models.CASCADE, related_name="events"
    )
    address = models.OneToOneField(
        "addresses.address", on_delete=models.CASCADE, related_name="event"
    )
