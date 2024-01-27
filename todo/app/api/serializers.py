from rest_framework import serializers
from django.contrib.auth.models import User
from app.models import ToDo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password']
        extra_kwargs = {"password":{'write_only': True}}

    def create(self,validated_data):
        user = User.objects.create_user(validated_data['username'],None,validated_data['password'])

        return user


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model=ToDo
        fields='__all__'

