from rest_framework import serializers
from .models import *

# Erzeugt aus einem queryset ein für python natives Datenformat für Device Types
class Device_TypeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=120)
    service_hours = serializers.IntegerField()
    conveying_capacity = serializers.DecimalField(max_digits=7, decimal_places=1)
    heating_up_time = serializers.IntegerField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    motor_error_code = serializers.CharField(max_length=7)
    oil_temperature = serializers.DecimalField(max_digits=7, decimal_places=2)
    operating_pressure = serializers.IntegerField()
    pump_rotational_frequency = serializers.IntegerField()
    components = serializers.CharField()

# Erzeugt aus einem queryset ein für python natives Datenformat für Devices
class DeviceSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=120)
    user = serializers.CharField()
    device_type = serializers.CharField()

# Erzeugt aus einem queryset ein für python natives Datenformat für Logs
class LogSerializer(serializers.Serializer):
    data = serializers.FloatField()
    timestamp = serializers.CharField()
    signal = serializers.IntegerField()
    device = serializers.CharField()
    notification = serializers.CharField()
