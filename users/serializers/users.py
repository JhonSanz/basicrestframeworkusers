""" User serializer definition """

from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.validators import UniqueValidator
from ..models import User


class UserSerializer(serializers.ModelSerializer):
    """ Defines user serializer behaviour. """

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = ["password", "profession", "email", "first_name",
                  "last_name"]

    def create(self, validated_data):
        return User.objects.create(
            **validated_data,
            password=make_password(validated_data.pop("password")),
            username=validated_data.get("email")
        )
