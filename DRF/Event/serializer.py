from rest_framework import serializers
from Event.models import *

from django.contrib.auth.models import User

class Event_Serielizer(serializers.ModelSerializer):
    class Meta:
        model=Event
        # fields="__all__"
        exclude=['image']

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



class Booking_Serielizer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields="__all__"


class TicketBookingSerializer(serializers.Serializer):
    event=serializers.IntegerField()
    ticket_type=serializers.CharField()
    total_person=serializers.IntegerField()
    user=serializers.IntegerField()

    def validate_event(self,value):
        if not Event.objects.filter(id=value,status="Happening").exists():
            raise serializers.ValidationError("Event Doesnot Exists")
        return value
    
    def validate_user(self,value):
        if not User.objects.filter(id=value).exists():
            raise serializers.ValidationError("User Doesn't Exists..")
        
    # def validate_total_person(self,value):
    #     event=Event.objects.filter()
    #     if value>

    def create(self, validated_data):
        event=Event.objects.get(id=validated_data.get('event'))
        user=User.objects.get(id=validated_data.get('user'))
        total_person=validated_data.get('total_person')
        ticket_type=validated_data.get("ticket_type")
        ticket=Ticket.objects.create(event=event,ticket_type=ticket_type,total_person=total_person)
        total_price=event.ticket_price * total_person
        booking=Booking.objects.create(
            ticket=ticket,
            user=user,
            status="PAID",
            total_price=total_price
        )
        return {
            "event":event.id,
            "ticket_type":ticket_type,
            "total_person":total_person,
            "user":user.id
        }

