from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):    
    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ['is_superuser']
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserDetailSerializer(serializers.ModelSerializer):
    ...
