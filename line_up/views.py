from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import LineUp
from .permissions import IsOwnerOrReadOnly
from .serializers import LineupDetailSerializer, LineupSerializer


class LineupView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = LineUp.objects.all()
    serializer_class = LineupSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LineupDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrReadOnly]

    queryset = LineUp.objects.all()
    lookup_url_kwarg = "lineup_id"
    serializer_class = LineupDetailSerializer
