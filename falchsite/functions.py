from .models import *
from django.utils import timezone
from django.shortcuts import render

def error_list(request):
    logs = Log.objects.all().order_by('timestamp').values('data', 'timestamp', 'signal', 'notification', 'device')
    errors = list(logs)
    # Aussortieren der Log Dateien ohne Fehlermeldung
    for l in logs:
        if l.get("signal") == 2:
            if (1000-int(l.get("data")))>50:
                errors.remove(l)

    # Aufschluesselung der Device ID zu Device Name und Hinzufuegen der Notification
    for e in errors:
        if e.get("signal") == 2:
            e["notification"] = "Service faellig"
        tmp = Device.objects.filter(id=int(e.get("device")))
        e["device"] = list(tmp)[1]
    return errors



