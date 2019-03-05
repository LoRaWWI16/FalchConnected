from django.conf.urls import url, include
#from .views import Device_TypesViewSet
from .views import DeviceViewSet

urlpatterns = [
#    url(r'device_types/', Device_TypesViewSet.as_view(), name="device_types-all")
    url(r'devices/', DevicesViewSet.as_view(), name="devices-all")
]
