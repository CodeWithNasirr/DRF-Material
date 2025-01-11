from django.urls import path,include
from .views import index,create_records,get_records,delete_records,subscribe_key,update_records,ValidateKeyView,create_student,get_student,update_student,create_user,get_book,StudentApi,StudentModel_view,StudentListCreate,StudentViewSet,RegisterAPi,LoginApi

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'v4/Student_Details',StudentViewSet,basename='Students')

urlpatterns = [
    path("api/",index,name="index"),
    path("api/subscribe_key",subscribe_key,name="subscribe_key"),
    path("api/create_records",create_records,name="Create_records"),
    path("api/update_records",update_records,name="Update_records"),
    path("api/get_records/",get_records,name="get_records"),
    path("api/delete_records",delete_records,name="delete_records"),
    path('api/validate-key/', ValidateKeyView.as_view(), name='validate-key'),
    path('api/create_student', create_student, name='create_book'),
    path('api/get_student', get_student, name='get_books'),
    path('api/update_student', update_student, name='update_book'),
    path('api/create_user', create_user, name='create_users'),
    path('api/get_book', get_book, name='get_books'),
    path('api/v1/Student_Details/', StudentApi.as_view()),
    path('api/v2/Student_Details/', StudentModel_view.as_view()),
    path('api/v3/Student_Details/', StudentListCreate.as_view()),
    path('api/register/', RegisterAPi.as_view()),
    path('api/LoginApi/', LoginApi.as_view()),
]

urlpatterns += router.urls