from dataclasses import fields

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
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['is_promoter', 'is_superuser']
        extra_kwargs = {'password': {'write_only': True}}


    def update(self, instance: User, validated_data: dict):

        if 'password' in validated_data.keys():
            password_data = validated_data.pop('password')
            instance.objects.set_password(password_data)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return super().update(instance, validated_data)
