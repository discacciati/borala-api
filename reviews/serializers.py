from events.serializers import EventSerializer
from rest_framework import serializers
from users.serializers import UserSerializer

from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

        read_only_fields = ["id"]


class ReviewDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = "__all__"

        read_only_fields = ["id"]
