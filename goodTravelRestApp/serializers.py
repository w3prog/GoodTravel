from rest_framework import serializers

from goodTravelRestApp.models import Address
from goodTravelRestApp.models import Place
from goodTravelRestApp.models import Plan
from goodTravelRestApp.models import User1
from goodTravelRestApp.models import Service, PlanPlace
from goodTravelRestApp.models import Feature


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User1
        fields = ('login', 'password', 'list_devices', 'language', 'budget', 'first_installation')


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ('country', 'region', 'locality', 'address', 'coordinates')


class FeatureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Feature
        fields = ('name','plan')


class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = ('name', 'type', 'description', 'address', 'image')


class PlanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plan
        fields = ('name', 'creator', 'budget', 'city')


class PlanPlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlanPlace
        fields = ('date', 'start_time', 'plan', 'service')


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ('name', 'price', 'start_time', 'end_time', 'image', 'place')
