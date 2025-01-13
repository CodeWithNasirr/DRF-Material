from rest_framework import serializers
from Event.models import *

from django.contrib.auth.models import User

class Event_Serielizer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields="__all__"

class Register_Serielizer(serializers.Serializer):
    username=serializers.CharField()
    email=serializers.EmailField()
    password=serializers.CharField()
    first_name=serializers.CharField()
    last_name=serializers.CharField()

    def validate_username(self,username):
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError("This username is already exists.....")


    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class Login_Serielizer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()

