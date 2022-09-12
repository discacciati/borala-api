from events.models import Event
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from .models import LineUp
from .permissions import IsEventOwner, IsOwnerOrReadOnly
from .serializers import LineupDetailSerializer, LineupSerializer


class LineupView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsEventOwner]

    queryset = LineUp.objects.all()
    serializer_class = LineupSerializer

    def get_queryset(self):
       return LineUp.objects.filter(event_id = self.kwargs["event_id"])

    def perform_create(self, serializer):
        event_id = self.kwargs["event_id"]
        event    = Event.objects.get(id=event_id)

        serializer.save(event=event)
    
    def post(self, request, *args, **kwargs):
        event_id = self.kwargs["event_id"]
        event    = Event.objects.get(id=event_id)

        self.check_object_permissions(request, event)
        return super().post(request, *args, **kwargs)

class LineupDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrReadOnly]

    queryset = LineUp.objects.all()
    lookup_url_kwarg = "lineup_id"
    serializer_class = LineupDetailSerializer
