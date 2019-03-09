from .models import *
from django.utils import timezone
from django.shortcuts import render

def error_list(request):
    logs = Log.objects.all().order_by('timestamp').values('data', 'timestamp', 'signal_id', 'module_id', 'notification_id')
    errors = logs
    for l in logs:
        if l.signal_id == 2:
            if (l.data - 1000)>50:
                errors.remove(l)
    return errors



