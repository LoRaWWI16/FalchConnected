from .models import *
from django.utils import timezone
from django.shortcuts import render

def error_list(request):
    logs = Log.objects.all().order_by('timestamp')
    for l in logs:
        print(l)
    return logs



