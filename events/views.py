from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView, Request, Response, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authtoken.models import Token
from rest_framework.mixins import CreateModelMixin

from .mixins import SerializerByMethodMixin

from .models import Event
from .serializers import EventSerializer, EventDetailedSerializer
from .permissions import IsOwnerOrReadyOnly

class EventView(SerializerByMethodMixin, generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrReadyOnly]
    
    queryset = Event.objects.all()

    serializer_map = {
        "GET": EventSerializer,
        "POST": EventDetailedSerializer,
    }

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
        
    #def get_queryset(self):
        #return self.queryset.order_by("-date")


class EventClosestDetailView(generics.ListAPIView):
    serializer_class = EventDetailedSerializer
    queryset = Event.objects.all()

    def get_queryset(self):

        return self.queryset.order_by("date")
    

class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrReadyOnly]
    
    queryset = Event.objects.all()
    
    serializer_class = EventDetailedSerializer
