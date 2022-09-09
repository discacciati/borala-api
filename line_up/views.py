from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import LineUp
from .permissions import IsOwnerOrReadOnly
from .serializers import LineupDetailSerializer, LineupSerializer
from events.models import Event


class LineupView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = LineUp.objects.all()
    serializer_class = LineupSerializer

    def perform_create(self, serializer):
        event_id = self.kwargs["event_id"]
        event    = Event.objects.get(id=event_id)

        serializer.save(event=event)


class LineupDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrReadOnly]

    queryset = LineUp.objects.all()
    lookup_url_kwarg = "lineup_id"
    serializer_class = LineupDetailSerializer
