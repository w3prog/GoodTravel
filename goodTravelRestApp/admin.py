from django.contrib import admin

# Register your models here.
from goodTravelRestApp.models import User1
from goodTravelRestApp.models import Place
from goodTravelRestApp.models import Address
from goodTravelRestApp.models import Date
from goodTravelRestApp.models import Plan

admin.register(User1)
admin.register(Place)
admin.register(Address)
admin.register(Date)
admin.register(Plan)
