from django.contrib.auth.models import User
from django.test import Client
from django.test import TestCase
from rest_framework.renderers import JSONRenderer
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory

from goodTravelRestApp.models import Address
from goodTravelRestApp.models import Place, PlanPlace
from goodTravelRestApp.models import Plan, Service
from goodTravelRestApp.models import User1, Feature
from goodTravelRestApp.serializers import AddressSerializer, FeatureSerializer
from goodTravelRestApp.serializers import PlaceSerializer, ServiceSerializer
from goodTravelRestApp.serializers import PlanSerializer, PlanPlaceSerializer
from goodTravelRestApp.serializers import UserSerializer


# Create your tests here.


class PersonTestCase(TestCase):
    def setUp(self):
        self.username = 'admin'
        self.password = 'secret'
        self.user = User.objects.create_user(self.username,
                                             'mail@example.com',
                                             self.password)
        self.user.is_staff = True
        self.user.is_superuser = True
        self.user.save()
        Address.objects.create(country="ddd", region="fgff", locality="gh", address="fg", coordinates="Fggg")
        User1.objects.create(login="1234", password="12345", list_devices="2345", language="gsg", budget="ghjhgfd",
                             first_installation="2016-12-22")
        Plan.objects.create(name="ffff", creator=User1.objects.get(id='1'), budget="ddddd", city="dfg")
        Feature.objects.create(name="fff", plan=Plan.objects.get(id='1'))
        Place.objects.create(name="sgg", type="sgsgsg", description="fgjdl", address=Address.objects.get(id='1'),
                             image="fffff")
        Service.objects.create(name="sgg", price="100", start_time="12:30", end_time="13:30",
                               image="fffff", place=Place.objects.get(id='1'))
        PlanPlace.objects.create(date="2016-12-22", start_time="12:30", plan=Plan.objects.get(id='1'),
                                 service=Service.objects.get(id='1'))

    def test_address(self):
        client = Client()
        client.login(username=self.username, password=self.password)
        response = client.get('/address/')
        self.assertEquals(response.status_code, 200)
        response = client.get('/address/1/')
        self.assertEquals(response.status_code, 200)
        address = Address.objects.get(id='1')
        content = JSONRenderer().render((AddressSerializer(address)).data)
        self.assertEqual(response.content, content)

    def test_user(self):
        client = Client()
        client.login(username=self.username, password=self.password)
        response = client.get('/users/')
        self.assertEquals(response.status_code, 200)
        response = client.get('/users/1/')
        self.assertEquals(response.status_code, 200)
        user = User1.objects.get(id='1')
        content = JSONRenderer().render((UserSerializer(user)).data)
        self.assertEqual(response.content, content)

    def test_place(self):
        factory = APIRequestFactory()
        request = factory.get('/')
        serializer_context = {
            'request': Request(request),
        }
        client = Client()
        client.login(username=self.username, password=self.password)
        response = client.get('/places/')
        self.assertEquals(response.status_code, 200)
        response = client.get('/places/1/')
        self.assertEquals(response.status_code, 200)
        p = Place.objects.get(id='1')
        s = PlaceSerializer(instance=p, context=serializer_context)
        content = JSONRenderer().render(s.data)
        self.assertEqual(response.content, content)

    def test_feature(self):
        factory = APIRequestFactory()
        request = factory.get('/')
        serializer_context = {
            'request': Request(request),
        }
        client = Client()
        client.login(username=self.username, password=self.password)
        response = client.get('/features/')
        self.assertEquals(response.status_code, 200)
        response = client.get('/features/1/')
        self.assertEquals(response.status_code, 200)
        p = Feature.objects.get(id='1')
        s = FeatureSerializer(instance=p, context=serializer_context)
        content = JSONRenderer().render(s.data)
        self.assertEqual(response.content, content)

    def test_plan(self):
        factory = APIRequestFactory()
        request = factory.get('/')
        serializer_context = {
            'request': Request(request),
        }
        client = Client()
        client.login(username=self.username, password=self.password)
        response = client.get('/plans/')
        self.assertEquals(response.status_code, 200)
        response = client.get('/plans/1/')
        self.assertEquals(response.status_code, 200)
        p = Plan.objects.get(id='1')
        s = PlanSerializer(instance=p, context=serializer_context)
        content = JSONRenderer().render(s.data)
        self.assertEqual(response.content, content)

    def test_service(self):
        factory = APIRequestFactory()
        request = factory.get('/')
        serializer_context = {
            'request': Request(request),
        }
        client = Client()
        client.login(username=self.username, password=self.password)
        response = client.get('/services/')
        self.assertEquals(response.status_code, 200)
        response = client.get('/services/1/')
        self.assertEquals(response.status_code, 200)
        p = Service.objects.get(id='1')
        s = ServiceSerializer(instance=p, context=serializer_context)
        content = JSONRenderer().render(s.data)
        self.assertEqual(response.content, content)

    def test_planPlace(self):
        factory = APIRequestFactory()
        request = factory.get('/')
        serializer_context = {
            'request': Request(request),
        }
        client = Client()
        client.login(username=self.username, password=self.password)
        response = client.get('/plan_place/')
        self.assertEquals(response.status_code, 200)
        response = client.get('/plan_place/1/')
        self.assertEquals(response.status_code, 200)
        p = PlanPlace.objects.get(id='1')
        s = PlanPlaceSerializer(instance=p, context=serializer_context)
        content = JSONRenderer().render(s.data)
        self.assertEqual(response.content, content)

    def tearDown(self):
        User1.objects.all().delete()
        User.objects.all().delete()
        Address.objects.all().delete()
        Plan.objects.all().delete()
        Place.objects.all().delete()
        PlanPlace.objects.all().delete()
        Service.objects.all().delete()
        Feature.objects.all().delete()
