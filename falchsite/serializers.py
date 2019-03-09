from rest_framework import serializers
from .models import *

class SignalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Signal
        fields = ("id", "name")

class ComponentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Component
        fields = ("name")

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

class PermissionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Permission
        fields = ("description")

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("email", "password", "permission")

class DeviceSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=120)
    user = serializers.CharField()
    device_type = serializers.CharField()

class NotificationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notification
        fields = ("name", "description")

class LogSerializer(serializers.Serializer):
    data = serializers.FloatField()
    timestamp = serializers.CharField()
    signal = serializers.CharField()
    device = serializers.CharField()
    notification = serializers.CharField()
