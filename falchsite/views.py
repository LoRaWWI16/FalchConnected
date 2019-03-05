# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.

class ListDevice_Types(generics.ListAPIView):
    """
    Provides a get method handler
    """
    queryset = Device_Type.name.all()
    serializers_class = Device_TypeSerializer
