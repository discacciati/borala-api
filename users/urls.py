from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from . import views

urlpatterns = [
    path("register/", views.UserRegisterView.as_view()),
    path("login/", ObtainAuthToken.as_view()),
    path("profile/", views.LoggedUserView.as_view()),
    path("users/", views.UserListView.as_view()),
    path("users/<uuid:user_id>/", views.UserDetailView.as_view()),
]
