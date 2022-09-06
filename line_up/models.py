import uuid

from django.db import models


class LineUp(models.Model):

    id = models.UUIDField(default=uuid.uuid4(), primary_key=True, editable=False)
    title = models.CharField(max_length=100, null=False)
    hour = models.TimeField(null=False)
    description = models.TextField()
    price = models.FloatField(default=0)
    id_event = models.UUIDField(default=uuid.uuid4)
    talent = models.TextField()

    event = models.ForeignKey(
        "events.Event", on_delete=models.CASCADE, related_name="lineup"
    )

    def __repr__(self) -> str:
        return f"Line-Up({self.title} - [{self.hour}])"
