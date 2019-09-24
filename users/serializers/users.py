import copy
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            validators=[UniqueValidator(queryset=User.objects.all())]
        )

    class Meta:
        model = User
        fields = ('username', 'password', 'profession',
                  'email', 'first_name', 'last_name')

    def create(self, validated_data):
        aux = copy.deepcopy(validated_data)
        if validated_data.get('password'):
            aux['password'] = make_password(
                validated_data['password']
            )
            user = User.objects.create(**aux)
            return user
