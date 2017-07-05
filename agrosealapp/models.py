from django.db import models

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return '{0} {1}'.format(self.first_name + ' ' + self.last_name)


class Company(models.Model):
    name = models.CharField(max_length=30)
    address = models.TextField()
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=11)
    contact_person = models.ForeignKey('Person')

    def __str__(self):
        return '{0}'.format(self.name)


class TruckDriver(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    address = models.TextField()
    license_number = models.CharField(max_length=20)
    company = models.ForeignKey('Company')
    referee = models.ForeignKey('Person')

    def __str__(self):
        return '{0} {1}'.format(self.first_name + ' ' + self.last_name)


class Truck(models.Model):
    driver = models.ForeignKey('TruckDriver')
    plate_number = models.CharField(max_length=8)
    vehicle_model = models.CharField(max_length=20)
    vehicle_type = models.CharField(max_length=20)

    def __str__(self):
        return '{0}'.format(self.plate_number)


class TrackDevice(models.Model):
    imei_number = models.UUIDField()
    driver = models.ForeignKey('TruckDriver')

    def __str__(self):
        return '{0}'.format(self.imei_number)


class TrackEvent(models.Model):
    device = models.ForeignKey('TrackDevice')
    current_longitude = models.DecimalField(max_digits=7, decimal_places=4)
    current_latitude = models.DecimalField(max_digits=7, decimal_places=4)
    current_address = models.TextField()
    created_on = models.DateTimeField()


class Request(models.Model):
    customer_phone = models.CharField(max_length=11)
    pickup_city = models.CharField(max_length=20)
    dropoff_city = models.CharField(max_length=20)
    fruit = models.CharField(max_length=10)
    fruit_quantity = models.IntegerField()
    service_date = models.DateField()
    service_time = models.TimeField()
    requested_on = models.DateTimeField(auto_now_add=True)


class Trip(models.Model):
    request = models.ForeignKey('Request')
    trip_cost = models.DecimalField(max_digits=7, decimal_places=2)
    income = models.DecimalField(max_digits=7, decimal_places=2)
