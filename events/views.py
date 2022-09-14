from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from django_filters import rest_framework as filters
from .models import Event
from .permissions import IsOwnerOrReadOnly, IsPromoterOrReadOnly
from .serializers import EventDetailedSerializer, EventSerializer

class EventListFilter(filters.FilterSet):
    date         = filters.DateFilter(field_name="date", lookup_expr="gte")
    title        = filters.CharFilter(field_name="title", lookup_expr="icontains")
    price        = filters.NumberFilter(field_name="price", lookup_expr="lte")
    category     = filters.CharFilter(field_name="categories__name", lookup_expr="iexact")
    state        = filters.CharFilter(field_name="address__state", lookup_expr="iexact")
    city         = filters.CharFilter(field_name="address__city", lookup_expr="icontains")
    district     = filters.CharFilter(field_name="address__district", lookup_expr="icontains")
    lineup_title = filters.CharFilter(field_name="lineup__title", lookup_expr="icontains")
    talent       = filters.CharFilter(field_name="lineup__talent", lookup_expr="icontains")

    class Meta:
        model  = Event
        fields = ["categories", "lineup", "address"]


class EventView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsPromoterOrReadOnly]

    queryset = Event.objects.all()

    serializer_class = EventSerializer
    filterset_class  = EventListFilter

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


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
