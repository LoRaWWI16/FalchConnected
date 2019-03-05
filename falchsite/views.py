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
    queryset = Device_Type.objects.all()
    serializers_class = Device_TypeSerializer
