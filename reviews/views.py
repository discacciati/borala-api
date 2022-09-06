from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from reviews.mixin import serializerByMethodMixin
from reviews.models import Review
from reviews.permissions import CustomProductPermission
from reviews.serializers import ReviewDetailSerializer, ReviewSerializer


class ReviewView(serializerByMethodMixin, generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    serializer_map = {
        "GET": ReviewSerializer,
        "POST": ReviewSerializer,
    }

    # DUVIDA
    #  def perform_create(self, serializer):
    #     serializer.save()


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [CustomProductPermission]

    queryset = Review.objects.all()
    serializer_class = ReviewDetailSerializer

    lookup_url_kwarg = "review_id"
