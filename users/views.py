from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView, Request, Response, status

from .models import User
from .permissions import IsOwnerPermission, IsSuperUserPermission
from .serializers import UserDetailSerializer, UserSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSuperUserPermission]


class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsOwnerPermission]
