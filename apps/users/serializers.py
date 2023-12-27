from apps.users.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


class UserCreateSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "confirm_password"
        ]
        extra_kwargs = {"password": {"write_only": True}, "confirm_password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        confirm_password = validated_data.pop('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError({"error": "Password does not match."})
        validated_data['password'] = make_password(password)
        user = User.objects.create(**validated_data)
        return user


class UserRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
        ]
