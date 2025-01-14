from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from Event.serializer import *
from Event.models import *
from rest_framework import viewsets
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from Event.permission import IsAdmin
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.decorators import action
from django.db.models import Q
# Create your views here.

class Register_Api(APIView):
    def post(self,request):
        data=request.data
        serializers=Register_Serielizer(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response({
                "status":True,
                "Message":"Account Created Successfully...",
                "data":serializers.data
            })
        else:
            return Response({
                "status":False,
                "Message":"Account Not Created Successfully...",
                "data":serializers.errors
            })



class Login_Api(APIView):
    def post(self,request):
        data=request.data
        serializers=Login_Serielizer(data=data)
        if serializers.is_valid():
            user=authenticate(username=serializers.data.get('username'),password=serializers.data.get('password'))
            if user:
                token,create=Token.objects.get_or_create(user=user)
                return Response({
                    "Status":True,
                    'Message':"Login Succesfully",
                    "data":{
                        "Token":token.key
                        }
                })
            else:
                return Response({
                    "Status":False,
                    'Message':"Invalid credentials",
                    "data":serializers.errors
                })
        return Response({
                    "Status":False,
                    'Message':"Login Failed",
                    "data":serializers.errors
        })




class Public_Event(viewsets.ModelViewSet):
    queryset=Event.objects.all()
    serializer_class=Event_Serielizer
    http_method_names=['get']

    @action(detail=False,methods=["GET"])
    def search_event(self,request):
        search=request.GET.get("search")
        query=Event.objects.all()
        if search:
            query=query.filter(Q(title__icontains=search)|Q(desc__icontains=search))
        serializers=Event_Serielizer(query,many=True)
        return Response({
                'Status':True,
                "Message":"Event Feched...",
                "Data":serializers.data
        })
    # def create(self, request, *args, **kwargs):
    #     raise MethodNotAllowed("Create not Allowed...")



class PrivateEvent_ModelViewSet(viewsets.ModelViewSet):
    queryset=Event.objects.all()
    serializer_class=Event_Serielizer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAdmin]



class Booking_ModelViewSet(viewsets.ModelViewSet):
    queryset=Booking.objects.all()
    serializer_class=Booking_Serielizer
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]

    @action(detail=False,methods=["POST"])
    def create_booking(self,request):
        data=request.data
        serializer=TicketBookingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "Status":True,
                'Message':"Booking Done",
                "Data":serializer.data
            })
        return Response({
                "Status":False,
                'Message':"Booking Not Done",
                "Data":serializer.errors
            })
    
    @action(detail=False,methods=["GET"])
    def get_booking(self,request):
        query=Booking.objects.all()
        serializers=Booking_Serielizer(query,many=True)
        return Response({
                "Status":True,
                'Message':"Booking Feteched...",
                "Data":serializers.data
            })