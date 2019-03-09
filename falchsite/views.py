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

class OneDeviceViewSet(APIView):

    def get(self, kwargs, id):
        deviceID = self.kwargs['id']
        queryset = Device.objects.filter(id=deviceID)
        serializer = DeviceSerializer(queryset, many=True)
        return Response({"devices": serializer.data})

class ErrorViewSet(APIView):

    def get(self, request):
        queryset = error_list(request)
        serializers = LogSerializer(queryset, many=True)
        return Response(serializers.data)
