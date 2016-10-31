from rest_framework import serializers

from goodTravelRestApp.models import Address
from goodTravelRestApp.models import Date
from goodTravelRestApp.models import Place
from goodTravelRestApp.models import Plan
from goodTravelRestApp.models import User1


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User1
        fields = ('login', 'password', 'list_devices', 'language', 'budget', 'first_installation')


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ('country', 'region', 'locality', 'address', 'coordinates')


class DateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Date
        fields = ('date', 'route', 'plan')


class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = ('name', 'type', 'description', 'address', 'image', 'day')


class PlanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plan
        fields = ('name', 'dates', 'creator', 'budget', 'city', 'users', 'features')
