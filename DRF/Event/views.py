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




class Event_ModelViewSet(viewsets.ModelViewSet):
    queryset=Event.objects.all()
    serializer_class=Event_Serielizer



class PrivateEvent_ModelViewSet(viewsets.ModelViewSet):
    queryset=Event.objects.all()
    serializer_class=Event_Serielizer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

