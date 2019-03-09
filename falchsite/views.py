# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from .functions import *
from django.http import QueryDict
from url_filter.filtersets import ModelFilterSet

# Create your views here.

class Device_TypesViewSet(APIView):

#    Provides a get method handler

    def get(self, request):
        #queryset = Device_Type.objects.all()
        queryset = Device_Type.objects.all().prefetch_related('components')
        serializer = Device_TypeSerializer(queryset, many=True)
        return Response({"device_types": serializer.data})


class DeviceViewSet(APIView):

    def get(self, request):
        queryset = Device.objects.all()
        serializer = DeviceSerializer(queryset, many=True)
        return Response({"devices": serializer.data})

"""class OneDeviceViewSet(APIView):

    def get(self, request):
        queryset = Device.objects.get()
        idURL = request.query_params.get('id', None)
        #queryset = Device.objects.all.filter(id=idURL)
        if (idURL != None):
            queryset = queryset.filter(id=idURL)
        serializer = DeviceSerializer(queryset, many=False)
        return Response({"device": serializer.data})
"""
class DeviceFilterSet(ModelFilterSet):
    class Meta(object):
        model = Device

query = QueryDict('id=1')
fs = DeviceFilterSet(data=query, queryset=Device.objects.all())
filtered_devices = fs.filter()

class ErrorViewSet(APIView):

    def get(self, request):
        queryset = error_list(request)
        serializers = LogSerializer(queryset, many=True)
        return Response({"errors": serializers.data})
