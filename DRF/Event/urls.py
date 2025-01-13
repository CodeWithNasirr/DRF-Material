from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'private_event',PrivateEvent_ModelViewSet,basename="private_events")
router.register(r'public_event',Public_Event,basename="public_event")
router.register(r'Booking',Booking_ModelViewSet,basename="Bookings")

urlpatterns = [
    path("register/",Register_Api.as_view(),name="registers"),
    path("login/",Login_Api.as_view(),name="Logins"),
]

urlpatterns+=router.urls