from django.db import models
import uuid

class Event(models.Model):
    id= models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=100, not_null=True)
    date = models.DateField(not_null=True)
    description = models.TextField()
    price = models.FloatField(null=True, blank=True, default="Gratuito")
    sponsor = models.CharField(max_length=50, null=True, blank=True)
    is_active = models.CharField(blank=True, null=True, default=True)
   
    categories = models.ManyToManyField("categories.category", on_delete=models.CASCADE , related_name="events" )
    user = models.ForeignKey("users.user", on_delete=models.CASCADE, related_name="events")
    address = models.ForeignKey("addresses.address", on_delete=models.CASCADE, related_name="event")
    