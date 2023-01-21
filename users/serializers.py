from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password


class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(
                queryset=CustomUser.objects.all(),
            )
        ],
    )

    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[
            validate_password,
        ],
        style={"input_type": "password"},
    )

    password2 = serializers.CharField(
        required=True,
        write_only=True,
        style={
            "input_type": "password",
        },
    )

    class Meta:
        model = CustomUser
        fields = [
            "email",
            "password",
            "password2",
        ]

    def validate(self, attrs):
        if attrs["password"] != attrs["password"]:
            raise serializers.ValidationError(
                {"Password": "Passwords must match"},
            )
        return

    def create(self, validated_data):
        user = CustomUser.objects.all(
            eamil=validated_data["email"],
        )
        user.set_password(
            validated_data["password"],
        )
        user.save()
