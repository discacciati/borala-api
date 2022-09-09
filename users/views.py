from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import User
from .permissions import IsSuperUserMethodOrOwner, IsSuperUserPermission
from .serializers import UserDetailSerializer, UserSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsSuperUserPermission]
    authentication_classes = [TokenAuthentication]


class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSuperUserMethodOrOwner]
    lookup_field = "id"
    lookup_url_kwarg = "user_id"
    admin_methods = ["DELETE", "GET"]
