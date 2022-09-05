from django.db import models


class Review(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.IntegerField()

    event = models.ForeignKey(
        "events.Event", on_delete=models.CASCADE, related_name="reviews"
    )

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="reviews"
    )
