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
            "cpf",
            "cnpj"
        ]
        read_only_fields  = ["id", "is_superuser"]
        extra_kwargs = {
            "password": {"write_only": True}, 
            "cpf": {"write_only": True}, 
            "cnpj": {"write_only": True}
            }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
    def validate_cpf(self, value):
        if not value.isnumeric() or len(value) != 11:
            raise serializers.ValidationError("CPF must be 11 numeric digits")

        return value
    
    def validate_cnpj(self, value):
        if not value.isnumeric() or len(value) != 14:
            raise serializers.ValidationError("CNPJ must be 14 numeric digits")

        return value


class UserReviewSerializer(serializers.ModelSerializer):
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
