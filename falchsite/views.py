# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from .functions import *

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

    def get(self, request):
        #queryset = Device.objects.get(id=kwargs['device_id'])
        queryset = Device.request.Get.get('id', '')
        serializer = DeviceSerializer(queryset, many=False)
        return Response({"device": serializer.data})

class ErrorViewSet(APIView):

    def get(self, request):
        queryset = error_list(request)
        serializers = DeviceSerializer(queryset, many=True)
        return Response({"errors": serializers.data})