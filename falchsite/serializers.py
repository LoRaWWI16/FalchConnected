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
    name = serializers.CharField(max_length=120)
    service_hours = serializers.IntegerField()
    components = serializers.CharField()

class PermissionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Permission
        fields = ("description")

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("email", "password", "permission")

class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = ("name", "user", "device_type")

class ModuleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Module
        fields = ("name", "device")

class NotificationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notification
        fields = ("name", "description")

class LogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Log
        fields = ("data", "timestamp", "signal", "module", "notification")