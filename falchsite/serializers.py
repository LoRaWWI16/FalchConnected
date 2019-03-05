from rest_framework import serializers
from .models import *

class SignalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signal
        fields = ("id", "name")

class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = ("name")

class Device_TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device_Type
        fields = ("name", "service_hours", "components")

class PermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ("description")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "password", "permission")

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ("name", "user", "device_type")

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ("name", "device")

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ("name", "description")

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ("data", "timestamp", "signal", "module", "notification")