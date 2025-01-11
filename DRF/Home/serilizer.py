from rest_framework import serializers
from .models import *
from datetime import datetime
from Home.validater import no_number
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
        age = current_date.year - instance.year
        return age
    
    def to_representation(self, instance):
        data= super().to_representation(instance)
        data['age']=self.calculate_age(instance.dob)
        return data

    def create(self, validated_data):# its same as #Custom Serilizer Method we use 
        return super().create(validated_data)
    
    def update(self, instance, validated_data):# its same as #Custom Serilizer Method we use 
        return super().update(instance, validated_data)

    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        if 'name' in data:
            data['name']=data['name'].strip().title()
        print(data['name'])
        return data
    
    def get_fields(self):# ye yaha per isliye use horaha jese koi user login karta hai to uska password show nahi hona chahiye
        field = super().get_fields()
        authenticate=True
        if authenticate:
            field.pop('password')
        return field


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


from rest_framework.validators import UniqueValidator
class User_Serilizer(serializers.Serializer):
    name=serializers.CharField(max_length=100,validators=[UniqueValidator(queryset=student.objects.all()),no_number])
    email=serializers.EmailField()
    age=serializers.IntegerField()
    user_type=serializers.ChoiceField(choices=['admin','user'])#it will show the choice in the dropdown
    admin_code=serializers.CharField(max_length=100,required=False)
    
    def validate(self, value):#here we can write all logic in one validate function
        # if 'email' in value and value['email'].split['@']=='gmail.com':
        #     raise serializers.ValidationError("Please Enter the Aycha  Email")
        

        if 'user_type' in value and value['user_type']=='admin' and 'admin_code' not in value:
            raise serializers.ValidationError("Admin code is required for admin user")


        if 'age' in value and value['age'] < 18 or value['age'] > 30:
            raise serializers.ValidationError("Age should be between 18 to 30")

        return value    


    def validate_age(self, value):#This is custom ValidATOR
        if value < 18 or value > 30:
            raise serializers.ValidationError("Age should be between 18 to 30")
        return value
    
    # def validate_email(self,value):
    #     if value.split['@']=='gmail.com':
    #         raise serializers.ValidationError("Please Enter the Aycha  Email")
    #     return value
    


class Author_Serilizer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields="__all__"

class Publisher_Serilizer(serializers.ModelSerializer):
    class Meta:
        model=Publisher
        fields="__all__"



class Book_Serilizer(serializers.ModelSerializer):
    author=Author_Serilizer()
    publisher=Publisher_Serilizer(many=True)
    class Meta:
        model=Book
        fields="__all__"

    
    def create(self, validated_data):
        author_data=validated_data.pop('author')
        publisher_datas=validated_data.pop('publisher')
        author,_=Author.objects.get_or_create(**author_data)
        book=Book.objects.create(author=author,**validated_data)
        for publisher_data in publisher_datas:
            publisher,_=Publisher.objects.get_or_create(**publisher_data)
            book.publisher.add(publisher)
        return book
    

from django.contrib.auth.models import User
class Register_Serilizer(serializers.Serializer):
    username=serializers.CharField(max_length=255)
    password=serializers.CharField(max_length=255)
    first_name=serializers.CharField(max_length=255)
    last_name=serializers.CharField(max_length=255)

    def validate_username(self,username):
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError("Username already exists...")
        
        return username
        
    def create(self, validated_data):
        username=validated_data['username']
        password=validated_data['password']
        first_name=validated_data['first_name']
        last_name=validated_data['last_name']
        user =User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name)
        return user


class Login_Serilizer(serializers.Serializer):
    username=serializers.CharField(max_length=255)
    password=serializers.CharField(max_length=255)