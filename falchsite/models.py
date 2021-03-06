from __future__ import unicode_literals

from django.db import models

# Create your models here.
# Datenbanktabelle signal
class Signal(models.Model):
    name = models.CharField(max_length=50)

#    def __str__(self):
#        return self.name

# Datenbanktabelle Component
class Component(models.Model):
    name = models.CharField(max_length=50)

#    def __str__(self):
#        return self.name

# Datenbanktabelle device_type mit m:n Beziehung zur Tabelle Component
class Device_Type(models.Model):
    name = models.CharField(max_length=50)
    service_hours = models.IntegerField(default=0)
    operating_pressure = models.IntegerField(default=0) #integer Arbeitsdruck
    conveying_capacity = models.DecimalField(default=0, max_digits=7, decimal_places=1) #decimal Foerdermenge
    pump_rotational_frequency = models.IntegerField(default=0) #Pumpendrehzahl IntegerField
    oil_temperature = models.DecimalField(default=0, max_digits=7, decimal_places=2) #Oeltemperatur
    motor_error_code = models.CharField(max_length=7, default='0') # Motorfehlercode Varchar (7)
    longitude = models.FloatField(default=0) #Standort Longitude Laengengrad float
    latitude = models.FloatField(default=0) # Standort Breitengrad float
    heating_up_time = models.IntegerField(default=0)# Aufheizzeit integer

    components = models.ManyToManyField(Component)

#    def __str__(self):
#        return self.name

# Datenbanktabelle permission
class Permission(models.Model):
    description = models.CharField(max_length=50)

#    def __str__(self):
#        return self.description

# Datenbanktabelle user mit Fremdschlüssel (1:n Beziehung) zur Tabelle permission
class User(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

#    def __str__(self):
#        return self.email

# Datenbanktabelle device mit einer 1:n Beziehung zur Tabelle device_type
class Device(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device_type = models.ForeignKey(Device_Type, on_delete=models.CASCADE)

#    def __str__(self):
#        return self.name

# Datenbanktabelle notification
class Notification(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

#    def __str__(self):
#        return self.name

# Datenbanktabelle log mit 1:n Beziehung zu  signal, notification und device
class Log(models.Model):
    data = models.CharField(max_length=128)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=False)
    signal = models.ForeignKey(Signal, on_delete=models.CASCADE)
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE, default=0)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
#    def __str__(self):
#        return self.data
