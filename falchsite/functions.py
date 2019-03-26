from .models import *
from django.utils import timezone
from django.shortcuts import render

def error_list(request):
    # Ausgabe aller Log Dateien absteigend nach Timestamp mit Limit 1000
    logs = Log.objects.all().order_by('-timestamp').values('data', 'timestamp', 'signal', 'notification', 'device')[:50]
    errors = list(logs)
    # Aussortieren der Log Dateien ohne Fehlermeldung
    for l in logs:
        # Ueberpruefen der Logs nach Signal ID ob Log Fehler meldet
        if l.get("signal") == 1:
            # Signal ID 1
            # Berechnet, ob maximale Lebenszeit ueberschritten
            if int(l.get("data"))<500:
                errors.remove(l)

        if l.get("signal") == 2:
            # Signal ID 2
            # Berechnet, ob Servicestunden faellig sind
 #           if (int(Device_Type.objects.filter(id=int(l.get("device"))).values("service_hours").first()["service_hours"])
 #               - int(l.get("data")))>50:
            if (5000-int(l.get("data"))>50):
                errors.remove(l)

        if l.get("signal") == 3:
            # Signal ID 3
            # Berechnet, ob Arbeitsdruck ueberschritten
            if float(l.get("data"))<250:
                errors.remove(l)

        if l.get("signal") == 4:
            # Signal ID 4
            # Berechnet, ob Foerdermenge ueberschritten
            if float(l.get("data"))<12:
                errors.remove(l)

        if l.get("signal") == 5:
            # Signal ID 5
            # Berechnet, ob Pumpendrehzahl ueberschritten
            if int(l.get("data"))<2500:
                errors.remove(l)

        if l.get("signal") == 6:
            # Signal ID 6
            # Berechnet, ob Oeltemperatur richtig
            if float(l.get("data")) < 65 and float(l.get("data")) > 40:
                errors.remove(l)

        if l.get("signal") == 10:
            # Signal ID 10
            # Berechnet, ob Aufheitzeit lang genug
            if int(l.get("data")) > 50:
                errors.remove(l)

        if l.get("signal") in [8,9]:
            # Signal ID 8, 9
            # Geben den Standort des Geraets an
            # Es handelt sich immer um Log Dateien, keine Fehler
            errors.remove(l)

    # Aufschluesselung der Device ID zu Device Name und Hinzufuegen der Notification
    for e in errors:
        # Notification bei Signal ID 1
        if e.get("signal") == 1:
            e["notification"] = "Ihr verwendetes Geraet ist sehr alt. Bitte schnellstmoeglich bei falch ein neues kaufen."
        # Notification bei Signal ID 2
        if e.get("signal") == 2:
            e["notification"] = "Service faellig"
        # Notification bei Signal ID 3
        if e.get("signal") == 3:
            e["notification"] = "Arbeitsdruck ueberpruefen"
        # Notification bei Signal ID 4
        if e.get("signal") == 4:
            e["notification"] = "Foerdermenge ueberpruefen"
        # Notification bei Signal ID 5
        if e.get("signal") == 5:
            e["notification"] = "Pumpendrehzahl ueberpruefen"
        # Notification bei Signal ID 6
        if e.get("signal") == 6:
            e["notification"] = "Oeltemperatur ueberpruefen"
        # Notification bei Signal ID 7
        if e.get("signal") == 7:
            e["notification"] = "Motor ueberpruefen"
        # Notification bei Signal ID 10
        if e.get("signal") == 10:
            e["notification"] = "Bitte vorgeschriebene Aufheizzeit des Geraets beachten"
        e["device"] = Device.objects.filter(id=int(e.get("device"))).values("name").first()["name"]
    return errors



