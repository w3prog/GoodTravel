from django.contrib import admin

# Register your models here.
from goodTravelRestApp.models import User1, Address, Place, Service, Plan, PlanPlace, Feature

admin.register(User1)
admin.register(Place)
admin.register(Address)
admin.register(Service)
admin.register(Plan)
admin.register(PlanPlace)
admin.register(Feature)
