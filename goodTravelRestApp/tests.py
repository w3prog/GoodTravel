from django.contrib.auth.models import User
from django.test import Client
from django.test import TestCase
from rest_framework.renderers import JSONRenderer
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory

from goodTravelRestApp.models import Address
from goodTravelRestApp.models import Date
from goodTravelRestApp.models import Place
from goodTravelRestApp.models import Plan
from goodTravelRestApp.models import User1
from goodTravelRestApp.serializers import AddressSerializer
from goodTravelRestApp.serializers import PlaceSerializer
from goodTravelRestApp.serializers import PlanSerializer
from goodTravelRestApp.serializers import UserSerializer
from goodTravelRestApp.serializers import DateSerializer


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
        Plan.objects.create(name="ffff", dates="29-23", creator=User1.objects.get(id='1'), budget="ddddd", city="dfg", users="dfff",
                            features="ddddd")
        Date.objects.create(date="2016-12-23", route="ggggggg", plan=Plan.objects.get(id='1'))
        Place.objects.create(name="sgg", type="sgsgsg", description="fgjdl", address=Address.objects.get(id='1'),
                              image="fffff", day=Date.objects.get(id='1'))


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

    def test_date(self):
        factory = APIRequestFactory()
        request = factory.get('/')
        serializer_context = {
            'request': Request(request),
        }
        client = Client()
        client.login(username=self.username, password=self.password)
        response = client.get('/days/')
        self.assertEquals(response.status_code, 200)
        response = client.get('/days/1/')
        self.assertEquals(response.status_code, 200)
        p = Date.objects.get(id='1')
        s = DateSerializer(instance=p, context=serializer_context)
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
