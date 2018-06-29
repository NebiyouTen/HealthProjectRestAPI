from rest_framework import serializers
from Registration.models import *

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'#('first_name','last_name','gender','date_of_birth','estimated_age','address')

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
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
    clients = ClientSerializer()
    class Meta:
        model = Calls
        fields = '__all__'#('phone_number','clients','is_owner','purpose','time','case_type','notes')

    def create(self, validated_data):
        client_data = validated_data.pop('clients')
        client = ClientSerializer.create(ClientSerializer(), validated_data=client_data)
        calls, created = Calls.objects.update_or_create(clients=client,**validated_data)
        #Client.objects.create(**client_data)
        return  calls

class ServiceSerializer(serializers.ModelSerializer):

    calls = CallsSerializer()
    staff = StaffSerializer()
    safe_spaces = Safe_SpacesSerializer()

    class Meta:
        model = Service
        fields = '__all__'#('calls','type','notes','internal','staff','safe_spaces')

class Police_Station_serviceSerializer(serializers.ModelSerializer):
    services = ServiceSerializer()
    police_stations = Police_StationsSerializer()
    class Meta:
        model = Police_Station_service
        fields = '__all__'#('services','police_stations')


class Health_Center_serviceSerializer(serializers.ModelSerializer):


    services = ServiceSerializer()
    health_centers = Health_CentersSerializer()
    class Meta:
        model = Health_Center_service
        fields = '__all__'#('services','health_centers')