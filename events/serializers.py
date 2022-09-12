from addresses.models import Address
from addresses.serializers import AddressSerializer
from categories.models import Category
from categories.serializers import CategorySerializer
from line_up.serializers import LineupSerializer
from rest_framework import serializers

from .models import Event


class EventSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(read_only=True, many=True)
    address = AddressSerializer(read_only=True)
    lineup = LineupSerializer(read_only=True, many=True)

    class Meta:
        model = Event
        fields = "__all__"
        read_only_fields = ["user"]


class EventDetailedSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    address = AddressSerializer()
    

    class Meta:
        model = Event
        fields = ["id","title", "date", "description", "price", "sponsor", "is_active", "categories", "address", "user_id" ]
        read_only_fields = ["id", "lineup", "categories"]
        depth = 1

    def create(self, validated_data: dict):
        categories_data = validated_data.pop("categories")
        address_data = validated_data.pop("address")

        address = Address.objects.create(**address_data)

        event: Event = Event.objects.create(**validated_data, address=address)

        for category in categories_data:
            category_created, _ = Category.objects.get_or_create(**category)

            event.categories.add(category_created)
            event.save()

        return event

    def update(self, instance: Event, validated_data: dict):

        if "address" in validated_data.keys():
            address_data = validated_data.pop("address")
            for key, value in address_data.items():
                setattr(instance.address, key, value)

        if "categories" in validated_data.keys():
            categories_data = validated_data.pop("categories")
            for category in categories_data:
                category_created, _ = Category.objects.get_or_create(**category)
                instance.categories.add(category_created)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
