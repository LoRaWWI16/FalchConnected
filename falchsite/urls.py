from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'device_types/', Device_TypesViewSet.as_view(), name="device_types-all"),
    url(r'devices/', DeviceViewSet.as_view(), name="devices-all"),
    url(r'devices/', DeviceViewSet.as_view(), name="devices-one"),
    url(r'logs/', ErrorViewSet.as_view(), name="logs-all")
]
