from rest_framework import serializers
from .models import Driver, Factory, Load


class DriverSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Driver
        fields = ['user_id', 'full_name']

class FactorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Factory
        fields = ['user_id', 'name']

class LoadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Load
        fields = ['weight', 'status']

    def create(self, validated_data):
        validated_data['factory'] = self.context.get('request').user.factory
        return Load.objects.create(**validated_data)