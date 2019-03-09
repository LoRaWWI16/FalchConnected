from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'device_types/', Device_TypesViewSet.as_view(), name="device_types-all"),
    url(r'devices/', DeviceViewSet.as_view(), name="devices-all"),
    url(r'^device/$', OneDeviceViewSet.as_view(), name="device_one"),
    url(r'errors', ErrorViewSet.as_view(), name="errors-all")
]
