import uuid

from django.core.validators import MaxValueValidator
from django.db import models


class Review(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.PositiveIntegerField(
        validators=[MaxValueValidator(5, "Ratings must be from 1 to 5")]
    )

    event = models.ForeignKey(
        "events.Event", on_delete=models.CASCADE, related_name="reviews"
    )

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="reviews"
    )
