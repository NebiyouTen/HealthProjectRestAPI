from django.db import models
import uuid

class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender_options = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=1, choices=gender_options,null=False)
    date_of_birth = models.DateField(null=True)
    estimated_age = models.IntegerField(null=True)
    address = models.CharField(max_length=200)
    def __str__(self):
        return self.first_name + self.last_name

class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)

class Safe_Spaces(models.Model):
    safe_space_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)

class Police_Stations(models.Model):
    police_station_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)

class Health_Centers(models.Model):
    health_center_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)

class Calls(models.Model):
    call_id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=15)
    clients = models.ForeignKey(Client,to_field="client_id", on_delete=models.CASCADE, null=True)
    is_owner = models.BooleanField()
    purpose = models.CharField(max_length=400)
    time = models.DateTimeField()
    case_types = (
        ('SX','Sexual Violence'),
        ('EC','Economic'),
        ('EM','Emotional'),
        ('PY', 'Physical'),
        ('OT', 'Other'),
    )
    case_type =  models.CharField(max_length=2,choices=case_types)
    notes = models.CharField(max_length=400)

class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    calls = models.ForeignKey(Calls, on_delete=models.CASCADE, null=True)
    type = models.CharField(max_length=200)
    notes = models.CharField(max_length=400)
    internal = models.BooleanField()

    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True)
    safe_spaces = models.ForeignKey(Safe_Spaces, on_delete=models.CASCADE, null=True)


class Police_Station_service(models.Model):
    police_station_service_id = models.AutoField(primary_key=True)
    services = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    police_stations = models.ForeignKey(Police_Stations, on_delete=models.CASCADE, null=True)

class Health_Center_service(models.Model):
    health_center_service_id = models.AutoField(primary_key=True)
    services = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    health_centers = models.ForeignKey(Health_Centers, on_delete=models.CASCADE, null=True)

