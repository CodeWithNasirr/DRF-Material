from django.contrib import admin
from Event.models import Event,Booking,Ticket
# Register your models here.

admin.site.register(Event)
admin.site.register(Booking) 
admin.site.register(Ticket) 
