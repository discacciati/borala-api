from django.urls import path

from reviews.views import ReviewDetail, ReviewView

urlpatterns = [
    path("events/<uuid:event_id>/reviews/", ReviewView.as_view()),
    path("events/<uuid:event_id>/reviews/<uuid:review_id>/", ReviewDetail.as_view()),
]
