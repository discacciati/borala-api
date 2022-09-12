from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
            "is_promoter",
            "is_superuser",
        ]
        read_only_fields = ["id", "is_superuser"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserReviewSerializeder(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name"]


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
            "is_promoter",
            "is_superuser",
        ]
        read_only_fields = ["id", "is_promoter", "is_superuser"]
        extra_kwargs = {"password": {"write_only": True}}

    def update(self, instance: User, validated_data: dict):

        if "password" in validated_data.keys():
            password_data = validated_data.pop("password")
            instance.set_password(password_data)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
