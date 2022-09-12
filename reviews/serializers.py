from rest_framework import serializers
from users.serializers import UserReviewSerializeder, UserSerializer

from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    user = UserReviewSerializeder(read_only=True)

    class Meta:
        model = Review
        fields = ["id", "title", "description", "rating", "user"]

        read_only_fields = ["id", "user"]
        depth = 1


class ReviewDetailSerializer(serializers.ModelSerializer):
    user = UserReviewSerializeder(read_only=True)

    class Meta:
        model = Review
        fields = ["id", "title", "description", "rating", "user"]

        read_only_fields = ["id", "user", "event"]

        depth = 1
