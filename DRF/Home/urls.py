from django.urls import path,include
from .views import index,create_records,get_records,delete_records,subscribe_key,update_records,ValidateKeyView,create_student,get_student,update_student
urlpatterns = [
    path("api/",index,name="index"),
    path("api/subscribe_key",subscribe_key,name="subscribe_key"),
    path("api/create_records/",create_records,name="Create_records"),
    path("api/update_records",update_records,name="Update_records"),
    path("api/get_records/",get_records,name="get_records"),
    path("api/delete_records",delete_records,name="delete_records"),
    path('api/validate-key/', ValidateKeyView.as_view(), name='validate-key'),
    path('api/create_student', create_student, name='create_book'),
    path('api/get_student', get_student, name='get_books'),
    path('api/update_student', update_student, name='update_book'),

] 