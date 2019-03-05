from django.conf.urls import url, include
from .views import Device_TypesViewSet

urlpatterns = [
    url(r'device_types/', Device_TypesViewSet.as_view(
        {
            'get': 'list'
        }
    ), name="device_types-all")
]