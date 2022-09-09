from events.serializers import EventSerializer
from rest_framework import serializers

from .models import LineUp


class LineupSerializer(serializers.ModelSerializer):
    class Meta:
        model  = LineUp
        fields = "__all__"
        read_only_fields = ['event']


class LineupDetailSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)

    class Meta:
        model = LineUp
        fields = "__all__"

        read_only_fields = ["id"]

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance,key,value)
        instance.save()

        return instance
