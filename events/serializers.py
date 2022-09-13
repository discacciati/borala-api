from addresses.models import Address
from addresses.serializers import AddressSerializer
from categories.models import Category
from categories.serializers import CategorySerializer
from line_up.serializers import LineupSerializer
from reviews.serializers import ReviewSerializer

from rest_framework import serializers

from .models import Event


class EventSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    address = AddressSerializer()

    class Meta:
        model = Event
        fields = [
            "id",
            "title", 
            "date", 
            "description", 
            "site_url",
            "price", 
            "sponsor", 
            "is_active", 
            "categories", 
            "address", 
            "user_id",
            "image_url",
        ]
        read_only_fields = ["user_id"]
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


class EventDetailedSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    address = AddressSerializer()
    lineup = LineupSerializer(read_only=True, many=True)
    reviews = ReviewSerializer(read_only=True, many=True)
    
    class Meta:
        model = Event
        fields = [
            "id",
            "title", 
            "date", 
            "description", 
            "site_url",
            "price", 
            "sponsor", 
            "is_active", 
            "categories", 
            "address", 
            "user_id",
            "image_url",
            "lineup",
            "reviews",
        ]

        read_only_fields = ["id", "lineup", "categories", "reviews"]
        depth = 1

    def update(self, instance: Event, validated_data: dict):

        if "address" in validated_data.keys():
            address_data = validated_data.pop("address")
            for key, value in address_data.items():
                setattr(instance.address, key, value)
            instance.address.save()

        if "categories" in validated_data.keys():
            categories_data = validated_data.pop("categories")
            for category in categories_data:
                category_created, _ = Category.objects.get_or_create(**category)
                instance.categories.add(category_created)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
