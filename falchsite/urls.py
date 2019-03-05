from django.conf.urls import url, include
from .views import ListDevice_Types

urlpatterns = [
    url(r'device_types/', ListDevice_Types.as_view(), name="device_types-all")
]