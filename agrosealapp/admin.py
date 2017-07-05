from django.contrib import admin
from .models import Truck, TruckDriver, Company, Person, TrackDevice

# Register your models here.
admin.site.register(Truck)
admin.site.register(TruckDriver)
admin.site.register(Company)
admin.site.register(Person)
admin.site.register(TrackDevice)
