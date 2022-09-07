from asyncore import read
from users.serializers import UserSerializer
from categories.serializers import CategorySerializer
from addresses.serializers import AddressSerializer
from rest_framework import serializers

from .models import Event, Category , Address


class EventSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(read_only=True)
    address = AddressSerializer(read_only=True)
    
    class Meta:
        model = Event
        fields = "__all__"
        read_only_fields = ["user"]
        
    def create(self, validated_data:dict):
        categories_data = validated_data.pop("categories")
        address_data = validated_data.pop("address")
        
        event: Event = Event.objects.create(**validated_data)
        
        for category in categories_data:
            category_created, _ = Category.objects.get_or_create(**category)
            event.categories.add(category_created)
        
        address_created, _ = Address.objects.create(**address_data)
        
        event.address.add(address_created)
        
        return event


class EventDetailedSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(read_only=True)
    address = AddressSerializer(read_only=True)
    
    class Meta:
        model = Event
        fields = "__all__"
        read_only_fields = ["id", "user" "is_superuser", "is_promoter"]
        
    def update(self, instance:Event, validated_data:dict):
        categories_data = validated_data.pop("categories")
        address_data = validated_data.pop("address")
        
        for key, value in validated_data.items():
            setattr(instance, key, value)
        
        for category in categories_data:
            category_created, _ = Category.objects.get_or_create(**category)
            instance.categories.add(category_created)
        
        for key, value in address_data.items():
            setattr(instance.address, key, value)
            
        instance.save()
        
        return instance
        
        
            
   
