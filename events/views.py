from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from .mixins import SerializerByMethodMixin
from .models import Event
from .permissions import IsOwnerOrReadOnly, IsPromoterOrReadOnly
from .serializers import EventDetailedSerializer, EventSerializer


class EventView(SerializerByMethodMixin, generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsPromoterOrReadOnly]

    queryset = Event.objects.all()

    serializer_map = {
        "GET": EventSerializer,
        "POST": EventDetailedSerializer,
    }

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # def get_queryset(self):
    # return self.queryset.order_by("-date")


class EventClosestDetailView(generics.ListAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def get_queryset(self):

        return self.queryset.order_by("date")


class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = "id"
    lookup_url_kwarg = "event_id"

    queryset = Event.objects.all()

    serializer_class = EventDetailedSerializer
