from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    # be able to read json and save a new user

    # the password field can be written but not read
    # if we add functionality to view all users, we don't want
    # the password hash to be exposed
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user

    class Meta:
        model = CustomUser
        fields = ("id", "username", "password", "email")  # we can add more
