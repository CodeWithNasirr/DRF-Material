from django.contrib import admin

# Register your models here.
from .models import Licence_Keys,student

admin.site.register(Licence_Keys)
admin.site.register(student)