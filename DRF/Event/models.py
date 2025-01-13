from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Event(models.Model):
    STATUS_CHOICES = [
        ("Upcoming", "Upcoming"),
        ("Cancelled", "Cancelled"),
        ("Happening", "Happening"),
    ]
    title=models.CharField(max_length=1000)
    desc=models.CharField(max_length=1000)
    date=models.DateField()
    capacity=models.IntegerField()
    ticket_price=models.FloatField(default=100)
    status=models.CharField(max_length=1000,default="Upcoming",choices=STATUS_CHOICES)
    image=models.ImageField(upload_to="Event_image")


class Ticket(models.Model):
    event=models.ForeignKey(Event,on_delete=models.CASCADE)
    ticket_type=models.CharField(max_length=100,choices=(("VIP","Vip"),("Normal","Normal")))
    total_person=models.IntegerField(blank=True,null=True)

class Booking(models.Model):
    ticket=models.ForeignKey(Ticket,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.CharField(max_length=100,default="Pending")
    total_price=models.FloatField(blank=True,null=True)

