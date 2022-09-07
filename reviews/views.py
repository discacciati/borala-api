from rest_framework import generics

from reviews.models import Review
from reviews.serializers import ReviewSerializer


class ReviewView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    ...
