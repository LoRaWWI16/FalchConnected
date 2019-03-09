from .models import *
from django.utils import timezone
from django.shortcuts import render

def error_list(request):
    logs = Log.objects.all().order_by('timestamp').values('data', 'timestamp', 'signal', 'device', 'notification')
    errors = list(logs)
    for l in logs:
        if l.get("signal") == 2:
            if (1000-int(l.get("data")))>50:
                errors.remove(l)

    return errors



