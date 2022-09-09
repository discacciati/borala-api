import uuid

from django.db import models


class LineUp(models.Model):

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=100, null=False)
    hour = models.TimeField(null=False)
    description = models.TextField()
    price = models.FloatField(default=0)
    talent = models.TextField()
    is_active = models.BooleanField(default=True)

    event = models.ForeignKey(
        "events.Event", on_delete=models.CASCADE, related_name="lineup"
    )
