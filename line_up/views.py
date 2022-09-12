from django.shortcuts import get_object_or_404
from events.models import Event
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from .models import LineUp
from .permissions import IsOwnerOrReadOnly
from .serializers import LineupDetailSerializer, LineupSerializer


class LineupView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrReadOnly]

    queryset = LineUp.objects.all()
    serializer_class = LineupSerializer

    def get_queryset(self):
       return LineUp.objects.filter(event_id = self.kwargs["event_id"])

    def perform_create(self, serializer):
        event_id = self.kwargs["event_id"]
        event    = Event.objects.get(id=event_id)

        serializer.save(event=event)

    def get_object(self):

        queryset = self.filter_queryset(self.get_queryset())
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}

        event_id = self.kwargs["event_id"]
        event    = Event.objects.get(id=event_id)

        obj = get_object_or_404(queryset, **filter_kwargs)
        self.check_object_permissions(self.request, event)

        return obj

class LineupDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrReadOnly]

    queryset = LineUp.objects.all()
    lookup_url_kwarg = "lineup_id"
    serializer_class = LineupDetailSerializer
