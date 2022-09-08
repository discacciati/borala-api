from rest_framework import serializers

from .models import LineUp


class LineupSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineUp
        fields = "__all__"

class LineupDetailSerializer(serializers.ModelSerializer):
    ...
