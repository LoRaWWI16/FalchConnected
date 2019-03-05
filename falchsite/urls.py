from django.urls import path
from .views import ListDevice_Types

urlpatterns = [
    path('device_types/', ListDevice_Types.as_view(), name="device_types-all")
]