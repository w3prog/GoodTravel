from rest_framework import viewsets

from goodTravelRestApp.models import Address
from goodTravelRestApp.models import Place
from goodTravelRestApp.models import Plan
from goodTravelRestApp.models import User1,Service,PlanPlace,Feature
from goodTravelRestApp.serializers import AddressSerializer
from goodTravelRestApp.serializers import PlaceSerializer
from goodTravelRestApp.serializers import PlanSerializer
from goodTravelRestApp.serializers import UserSerializer,ServiceSerializer,PlanPlaceSerializer,FeatureSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = User1.objects.all()
    serializer_class = UserSerializer


class AddressViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class PlanViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


class FeatureViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer


class PlaceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class PlanPlaceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = PlanPlace.objects.all()
    serializer_class = PlanPlaceSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
