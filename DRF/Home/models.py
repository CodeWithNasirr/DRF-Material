from django.db import models

# Create your models here.


class Licence_Keys(models.Model):
    key=models.CharField(max_length=100,unique=True)
    device_id=models.CharField(max_length=100,blank=True,null=True)
    # is_active=models.BooleanField(default=False)

    def __str__(self):
        return f"ID-{self.id} Keys: {self.key}"
    

class student(models.Model):
    name=models.CharField(max_length=100)
    # age=models.IntegerField()
    dob=models.DateField(null=True,blank=True)
    email=models.EmailField()
    password=models.CharField(max_length=100)

    def __str__(self):
        return f"ID-{self.id} Name: {self.name}"
    

class Author(models.Model):
    name=models.CharField(max_length=100)

class Publisher(models.Model):
    name=models.CharField(max_length=100)
    website=models.URLField()

class Book(models.Model):
    Book_title=models.CharField(max_length=100)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name='book_publisher')
    publisher=models.ManyToManyField(Publisher,related_name='books')