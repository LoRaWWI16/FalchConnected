# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework.views import APIView
from .models import *
from .serializers import *

# Create your views here.

class Device_TypesViewSet(APIView):
    """
    Provides a get method handler
    """
    def get(self, request):
        queryset = Device_Type.objects.all()
        serializer = Device_TypeSerializer(queryset, many=True)
        return Response({"device types": serializer.data})
