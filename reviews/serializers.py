from rest_framework import serializers
from users.serializers import UserReviewSerializer, UserSerializer

from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    user = UserReviewSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ["id", "title", "description", "rating", "user"]

        read_only_fields = ["id", "user"]
        depth = 1


class ReviewDetailSerializer(serializers.ModelSerializer):
    user = UserReviewSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ["id", "title", "description", "rating", "user"]

        read_only_fields = ["id", "user", "event"]

        depth = 1
