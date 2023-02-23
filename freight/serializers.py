from rest_framework import serializers
from .models import Driver, Factory


class DriverSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Driver
        fields = ['user_id', 'full_name']

class FactorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Factory
        fields = ['user_id', 'name']
