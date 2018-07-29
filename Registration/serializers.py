from rest_framework import serializers
from Registration.models import *

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'#'('client_id','first_name','last_name','date_of_birth','estimated_age','address')
        depth = 1

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'#('first_name','last_name','address','designation')

class Automated_callSerializer(serializers.ModelSerializer):
    class Meta:
        model = Automated_call
        fields = '__all__'#('first_name','last_name','address','designation')

class Safe_SpacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Safe_Spaces
        fields = '__all__'#('name','location')

class Police_StationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Police_Stations
        fields = '__all__'#('name','location')

class Health_CentersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Health_Centers
        fields = '__all__'#('name','location')

class CallsSerializer(serializers.ModelSerializer):

    clients = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    class Meta:

        model = Calls
        fields = '__all__'#('phone_number','clients','is_owner','purpose','time','case_type','notes')
        depth = 1

    def create(self, validated_data):
        client_data = validated_data.pop('clients')
        client = Client.objects.get(client_id=client_data.client_id)
        calls = Calls.objects.create(clients=client,**validated_data)
        return  calls

class ServiceSerializer(serializers.ModelSerializer):
    calls = serializers.PrimaryKeyRelatedField(queryset=Calls.objects.all())
    staff = serializers.PrimaryKeyRelatedField(queryset=Staff.objects.all())
    safe_spaces = serializers.PrimaryKeyRelatedField(queryset=Safe_Spaces.objects.all())

    class Meta:
        model = Service
        fields = '__all__'#('calls','type','notes','internal','staff','safe_spaces')

    def create(self, validated_data):
        calls_data = validated_data.pop('calls')
        staff_data = validated_data.pop('staff')
        safe_spaces = validated_data.pop('safe_spaces')

        call = Calls.objects.get(call_id=calls_data.call_id)
        staff = Staff.objects.get(staff_id=staff_data.staff_id)
        safe_spaces = Safe_Spaces.objects.get(safe_space_id=safe_spaces.safe_space_id)

        service = Service.objects.create(calls=call,staff=staff,
                                                            safe_spaces=safe_spaces, **validated_data)

        return service

class Police_Station_serviceSerializer(serializers.ModelSerializer):
    services = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all())
    police_stations = serializers.PrimaryKeyRelatedField(queryset=Police_Stations.objects.all())
    class Meta:
        model = Police_Station_service
        fields = '__all__'#('services','police_stations')

    def create(self, validated_data):
        services_data = validated_data.pop('services')
        police_stations_data = validated_data.pop('police_stations')

        services = Service.objects.get(service_id =
                                       services_data.service_id)

        police_stations = Police_Stations.objects.get(police_station_id =
                                                      police_stations_data.police_station_id)

        service = Police_Station_service.objects.create(services=services,police_stations=police_stations,
                                                            **validated_data)
        return service



class Health_Center_serviceSerializer(serializers.ModelSerializer):


    services = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all())
    health_centers = serializers.PrimaryKeyRelatedField(queryset=Health_Centers.objects.all())
    class Meta:
        model = Health_Center_service
        fields = '__all__'#('services','health_centers')

    def create(self, validated_data):

        services_data = validated_data.pop('services')
        health_centers_data = validated_data.pop('health_centers')

        services = Service.objects.get(service_id=
                                       services_data.service_id)

        health_centers = Health_Centers.objects.get(health_center_id
                                                  = health_centers_data.health_center_id)

        service = Health_Center_service.objects.create(services=services,health_centers=health_centers,
                                                            **validated_data)
        return service
