from django.urls import path,include

urlpatterns = [
    path("event/",include('Event.urls')),
]
