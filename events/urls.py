from django.urls import path
from . import views

urlpatterns = [
    path("events/", views.EventView.as_view()),
    path("events/closest/", views.EventClosestDetailView.as_view()),
    path("events/<uuid:event_id>/", views.EventDetailView.as_view()),
]
