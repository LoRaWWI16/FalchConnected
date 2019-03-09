from .models import *
from django.utils import timezone
from django.shortcuts import render

def error_list(request):
    logs = Log.objects.all().order_by('timestamp').values('data', 'timestamp', 'signal', 'notification')
    errors = list(logs)
    # Aussortieren der Log Dateien ohne Fehlermeldung
    for l in logs:
        if l.get("signal") == 2:
            if (1000-int(l.get("data")))>50:
                errors.remove(l)

    # Aufschluesselung der Device ID zu Device Name
#    for e in errors:
#        e[4] = Device.objects.filter(id=int(e.get("device"))).get("name")
    return errors



