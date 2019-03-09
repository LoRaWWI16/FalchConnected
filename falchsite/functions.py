from .models import *
from django.utils import timezone
from django.shortcuts import render

def error_list(request):
    logs = Log.objects.all().order_by('timestamp').values('data', 'timestamp', 'signal_id', 'module_id', 'notification_id')
    errors = logs
    for l in logs:
        if l.get("signal_id") == 2:
            if (1000-l.get("signal_id"))>50:
                errors.remove(l)
    return errors



