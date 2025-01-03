from rest_framework import serializers
from .models import Licence_Keys,student
from datetime import datetime

class Licence_key_Serializers(serializers.ModelSerializer):
    class Meta:
        model=Licence_Keys
        fields="__all__"
        # exclude=['key','id'] if u want to remove any field from the model then u use this one



class Student_Serialiser(serializers.ModelSerializer):
    class Meta:
        model=student
        fields="__all__"


    def calculate_age(self,instance):
        current_date=datetime.now()
        age=current_date.year-instance.year
        return age
    
    def to_representation(self, instance):
        data= super().to_representation(instance)
        data['age']=self.calculate_age(instance.dob)
        return data

#Custom Serilizer Method
# class Student_Serialiser(serializers.Serializer):
#     id=serializers.IntegerField()
#     name=serializers.CharField(max_length=100)
#     age=serializers.IntegerField()
#     email=serializers.EmailField()
#     password=serializers.CharField(max_length=100)
        
#     #it work like a signal when the funcion is called then it automatically call the to_representation function
#     def to_representation(self, instance):
#         return super().to_representation(instance)
    


#     def update(self, instance, validated_data):
#         id=validated_data.get("id",instance.id)
#         name=validated_data.get("name",instance.name)
#         age=validated_data.get("age",instance.age)
#         email=validated_data.get("email",instance.email)
#         password=validated_data.get("password",instance.password)
#         instance.id=id
#         instance.name=name
#         instance.age=age
#         instance.email=email
#         instance.password=password
#         instance.save()
#         return instance

#     def create(self, validated_data):
#         Student=student.objects.create(**validated_data)
#         return Student