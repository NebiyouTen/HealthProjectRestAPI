from .models import *
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.constants import ALL, ALL_WITH_RELATIONS

class StaffResource(ModelResource):

    class Meta:
        queryset = Staff.objects.all()
        resource_name = 'staff'
        authorization = Authorization()

class Safe_SpacesResource(ModelResource):

    class Meta:
        queryset = Safe_Spaces.objects.all()
        resource_name = 'safe_spaces'
        authorization = Authorization()

class Police_StationsResource(ModelResource):
    class Meta:
        queryset = Police_Stations.objects.all()
        resource_name = 'police_stations'
        authorization = Authorization()

class Health_CentersResource(ModelResource):
    class Meta:
        queryset = Health_Centers.objects.all()
        resource_name = 'health_centers'
        authorization = Authorization()

class ClientsResource(ModelResource):
    class Meta:
        filtering = {
            "phone_number": ALL,
            "gender": ALL,
        }
        queryset = Client.objects.all()
        resource_name = 'clients'
        authorization = Authorization()



class CallsResource(ModelResource):
    clients = fields.ForeignKey(ClientsResource, 'clients')
    class Meta:
        queryset = Calls.objects.all()
        resource_name = 'calls'
        authorization = Authorization()
        filtering = {
            'client': ALL_WITH_RELATIONS,
        }


class ServicesResource(ModelResource):
    calls = fields.ForeignKey(CallsResource, 'calls', null=True, blank=True)
    staff = fields.ForeignKey(StaffResource, 'staff', null=True, blank=True)
    safe_spaces = fields.ForeignKey(Safe_SpacesResource, 'safe_spaces', null=True, blank=True)
    class Meta:
        queryset = Service.objects.all()
        resource_name = 'services'
        authorization = Authorization()


class Police_Station_serviceResource(ModelResource):
    services = fields.ForeignKey(ServicesResource, 'services', null=True, blank=True)
    police_stations = fields.ForeignKey(Police_StationsResource, 'police_stations', null=True, blank=True)
    class Meta:
        queryset = Police_Station_service.objects.all()
        resource_name = 'police_station_services'
        authorization = Authorization()


class Health_Center_serviceResource(ModelResource):
    services = fields.ForeignKey(ServicesResource, 'services', null=True, blank=True)
    health_centers = fields.ForeignKey(Health_CentersResource, 'health_centers', null=True, blank=True)
    class Meta:
        queryset = Health_Center_service.objects.all()
        resource_name = 'health_center_services'
        authorization = Authorization()







