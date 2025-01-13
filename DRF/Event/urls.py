from django.urls import path,include
from .views import *
urlpatterns = [
    path("register/",Register_Api.as_view(),name="registers"),
    path("login/",Login_Api.as_view(),name="Logins"),
]