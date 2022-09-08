from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from . import views

urlpatterns = [
    path("register/", views.UserView.as_view()),
    path("login/", ObtainAuthToken.as_view()),
    path("users/", views.UserView.as_view()),
    path("users/<uuid:user_id>/", views.UserDetailView.as_view()),
]
