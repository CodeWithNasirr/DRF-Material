from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Licence_Keys,student,Book
from Home.serilizer import Licence_key_Serializers,Student_Serialiser,User_Serilizer,Book_Serilizer
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.
@api_view(['GET'])
def index(request):
    data={
        'name':'Aman',
        'age':20
    }
    return Response(data)


@api_view(["POST","GET","DELETE"])
def subscribe_key(request):
    if request.method=="GET":
        #This is For Single details
        if request.GET.get('id'):
            querys=Licence_Keys.objects.get(id=request.GET.get('id'))
            serelizer=Licence_key_Serializers(querys)
        # # data=[{
        #     'key':values.key,

        # } for values in Licence_Keys.objects.all()]

        # This is For Multiple details
        else:
            querys=Licence_Keys.objects.all()
            serelizer=Licence_key_Serializers(querys,many=True)

        return Response({
            'status':True,
            'data':serelizer.data,
        })
    elif request.method=="POST":
        data=request.data
        Licence_Keys.objects.create(**data)
        return Response({
            'status':True,
            'Message':'Record Created'
        })
    elif request.method=="DELETE":
        Licence_Keys.objects.filter(id=request.GET.get('id')).delete()
        return JsonResponse({
            'status':True,
            'Message':'Record Deleted'
        })


@api_view(["POST"])
def create_records(request):
    data=request.data
    serilizer=Licence_key_Serializers(data=data)
    if not serilizer.is_valid():
        return Response({
            'status':False,
            'Messsage':'Record Not Created',
            "error":serilizer.errors,
        })
    serilizer.save()
    # Licence_Keys.objects.create(**data)
    print(data)
    return Response({
        'status':True,
        'Messsage':'Record Created'
    })

@api_view(["PATCH"])
def update_records(request):
    data=request.data
    if not request.GET.get('id'):
        return Response({
            'status':False,
            'Messsage':'Record Not Updated',
            "error":"Id is Required",
        })
    keys=Licence_Keys.objects.get(id=request.GET.get('id'))
    serelizer=Licence_key_Serializers(keys,data=data,partial=True)
    if not serelizer.is_valid():
            return Response({
            'status':False,
            'Messsage':'Record Not Updated',
            "error":serelizer.errors,
        })
    serelizer.save()
    return Response({
            'status':True,
            'Messsage':'Record  Updated Sucessfully',
            "data":serelizer.data,
        })


@api_view(["GET"])
def get_records(request):
    if request.GET.get('id'):
        querys=Licence_Keys.objects.all(id=request.GET.get('id'))
        serilizer=Licence_key_Serializers(querys)
    else:
        querys=Licence_Keys.objects.all()
        serilizer=Licence_key_Serializers(querys,many=True)
    return Response(({
        'status':True,
        'data':serilizer.data,
    }))

@api_view(["DELETE"])
def delete_records(request):
    Licence_Keys.objects.filter(id=request.GET.get('id')).delete()
    return JsonResponse({
        'status':True,
        'Message':'Record Deleted'
    })


@api_view(["POST"])
def create_user(request):
    data=request.data
    # serilizer=User_Serilizer(data=data)
    serilizer=Book_Serilizer(data=data)
    if not serilizer.is_valid():
        return Response({
            'status':False,
            'Messsage':'Record Not Created',
            "error":serilizer.errors,
        })
    serilizer.save()
    return  Response({
        'status':True,
        "data":serilizer.data,
    })

@api_view(["GET"])
def get_book(request):
    if request.GET.get('id'):
        querys=Book.objects.get(id=request.GET.get('id'))
        serilizer=Book_Serilizer(querys)
    else:
        querys=Book.objects.all()
        serilizer=Book_Serilizer(querys,many=True)
    return Response(({
        'status':True,
        'data':serilizer.data,
    }))



#Custom Serilizer Method
@api_view(["POST"])
def create_student(request):
    data=request.data
    serilizer=Student_Serialiser(data=data)
    if not serilizer.is_valid():
        return Response({
            'status':False,
            'Messsage':'Record Not Created',
            "error":serilizer.errors,
        })
    # serilizer.save()
    # Licence_Keys.objects.create(**data)
    serilizer.save()
    return Response({
        'status':True,
        'Messsage':'Record Created'
    })

#Validation Serelizer
@api_view(["GET"])
def get_student(request):
    if request.GET.get('id'):
        querys=student.objects.get(id=request.GET.get('id'))
        serilizer=Student_Serialiser(querys)
    else:
        querys=student.objects.all()
        serilizer=Student_Serialiser(querys,many=True)
    return Response(({
        'status':True,
        'data':serilizer.data,
    }))

@api_view(["PATCH"])
def update_student(request):
    data=request.data
    if not request.GET.get('id'):
        return Response({
            'status':False,
            'Messsage':'Record Not Updated',
            "error":"Id is Required",
        })
    keys=student.objects.get(id=request.GET.get('id'))
    serelizer=Student_Serialiser(keys,data=data,partial=True)
    if not serelizer.is_valid():
            return Response({
            'status':False,
            'Messsage':'Record Not Updated',
            "error":serelizer.errors,
        })
    serelizer.save()
    return Response({
            'status':True,
            'Messsage':'Record  Updated Sucessfully',
            "data":serelizer.data,
        })
@api_view(["DELETE"])
def delete_student(request):
    student.objects.fillter(id=request.GET.get("id")).delete()
    return JsonResponse({
        'status':True,
        'Message':'Record Deleted'
    })

# ABout Api View
class StudentApi(APIView):
    def post(self,request):
        data=request.data
        serilizer=Student_Serialiser(data=data)
        if not serilizer.is_valid():
            return Response({
                'status':False,
                'Messsage':'Record Not Created',
                "error":serilizer.errors,
            })
        # serilizer.save()
        # Licence_Keys.objects.create(**data)
        serilizer.save()
        return Response({
            'status':True,
            'Messsage':'Record Created'
        })

    def get(self,request):
        if request.GET.get('id'):
            querys=student.objects.get(id=request.GET.get('id'))
            serilizer=Student_Serialiser(querys)
        else:
            querys=student.objects.all()
            serilizer=Student_Serialiser(querys,many=True)
        return Response(({
            'status':True,
            'data':serilizer.data,
        }))

    def patch(self,request):
        data=request.data
        if not request.GET.get('id'):
            return Response({
                'status':False,
                'Messsage':'Record Not Updated',
                "error":"Id is Required",
            })
        keys=student.objects.get(id=request.GET.get('id'))
        serelizer=Student_Serialiser(keys,data=data,partial=True)
        if not serelizer.is_valid():
                return Response({
                'status':False,
                'Messsage':'Record Not Updated',
                "error":serelizer.errors,
            })
        serelizer.save()
        return Response({
                'status':True,
                'Messsage':'Record  Updated Sucessfully',
                "data":serelizer.data,
            })

    def delete(self,request):
        student.objects.fillter(id=request.GET.get("id")).delete()
        return JsonResponse({
            'status':True,
            'Message':'Record Deleted'
        })

# About ListMix,Generic_view,Etc..
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin
from rest_framework.generics import GenericAPIView
class StudentModel_view(ListModelMixin,CreateModelMixin,UpdateModelMixin,GenericAPIView):
    queryset=student.objects.all()
    serializer_class=Student_Serialiser
    
    def get_queryset(self):
        return student.objects.filter(name__startswith="n")

    def perform_create(self, serializer):
        return super().perform_create(serializer)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)





class ValidateKeyView(APIView):
    def post(self, request, format=None):
        key = request.data.get('key')
        device_id = request.data.get('device_id')

        try:
            # Check if the key exists in the database
            subscription_key = Licence_Keys.objects.get(key=key)

            # Case 1: Enter 1st time key on your device
            if not subscription_key.device_id:
                subscription_key.device_id = device_id
                subscription_key.save()
                return Response(
                    {"message": "Key validated successfully"},
                    status=status.HTTP_200_OK,
                )
            # Case 2: if You vip Json id == Django data id same then it work
            elif subscription_key.device_id == device_id:
                print("== Work")
                return Response(
                {"message": "Key already in use on this device"},
                status=status.HTTP_202_ACCEPTED,
            )
             # Case 3: Key is already used on a different device
            elif subscription_key.device_id and subscription_key.device_id != device_id:
                print("Device not Matched")
                return Response(
                    {"message": "Key already in use on another device"},
                    status=status.HTTP_403_FORBIDDEN,
                )
        except Licence_Keys.DoesNotExist:
            # Case 4: Invalid key
            return Response(
                {"message": "Invalid key"},
                status=status.HTTP_404_NOT_FOUND,
            )