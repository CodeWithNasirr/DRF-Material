from django.contrib import admin

# Register your models here.
from .models import Licence_Keys,student,Book,Author,Publisher

admin.site.register(Licence_Keys)
admin.site.register(student)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)