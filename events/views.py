from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from .mixins import FilterByQueryParamsMixin, SerializerByMethodMixin
from .models import Event
from .permissions import IsOwnerOrReadOnly, IsPromoterOrReadOnly
from .serializers import EventDetailedSerializer, EventSerializer


class EventView(FilterByQueryParamsMixin, SerializerByMethodMixin, generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsPromoterOrReadOnly]

    queryset = Event.objects.all()

    serializer_map = {
        "GET": EventSerializer,
        "POST": EventDetailedSerializer,
    }

    querystring_map = {
        'date':'date',
        'title':'title__icontains',
        'category':'category__name__iexact',
        'state':'address__state__exact',
        'city':'address__city__icontains',
        'district':'address__district__icontains',
        'lineup_title':'lineup__title__icontains',
        'talent':'lineup__talent__icontains',
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
