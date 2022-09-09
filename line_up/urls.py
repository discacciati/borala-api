from django.urls import path
from . import views

urlpatterns = [
    path("events/<uuid:event_id>/lineup/", views.LineupView.as_view()),
    path("events/<uuid:event_id>/lineup/<uuid:lineup_id>/", views.LineupDetailView.as_view()),
]
