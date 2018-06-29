# from .models import *
# #from tastypie.authentication import BasicAuthentication
# from django.contrib.auth.models import User
# #from tastypie.constants import ALL, ALL_WITH_RELATIONS
#
# #from tastypie.resources import ModelResource
# #from tastypie.authorization import DjangoAuthorization
# #from tastypie import fields
#
# #from Registration.authentication import OAuth20Authentication
#
#
# class UserResource(ModelResource):
#
#     class Meta:
#         queryset = User.objects.all()
#         resource_name = 'user'
#         excludes = ["email","password","is_superuser","id"]
#         allowed_methods = ['get']
#         authorization = DjangoAuthorization()
#         authentication = BasicAuthentication()
#
# class StaffResource(ModelResource):
#
#     class Meta:
#         queryset = Staff.objects.all()
#         resource_name = 'staff'
#         authorization = DjangoAuthorization()
#         authentication = BasicAuthentication()
#
# class Safe_SpacesResource(ModelResource):
#
#     class Meta:
#         queryset = Safe_Spaces.objects.all()
#         resource_name = 'safe_spaces'
#         authorization = DjangoAuthorization()
#         authentication = BasicAuthentication()
#
# class Police_StationsResource(ModelResource):
#
#     class Meta:
#         queryset = Police_Stations.objects.all()
#         resource_name = 'police_stations'
#         authorization = DjangoAuthorization()
#         authentication = BasicAuthentication()
#
# class Health_CentersResource(ModelResource):
#
#     class Meta:
#         queryset = Health_Centers.objects.all()
#         resource_name = 'health_centers'
#         authorization = DjangoAuthorization()
#         authentication = BasicAuthentication()
#
# class ClientsResource(ModelResource):
#     class Meta:
#         filtering = {
#             "phone_number": ALL,
#             "gender": ALL,
#         }
#         queryset = Client.objects.all()
#         resource_name = 'clients'
#         authorization = DjangoAuthorization()
#         authentication = BasicAuthentication()
#
#
# class CallsResource(ModelResource):
#     clients = fields.ForeignKey(ClientsResource, 'clients')
#     class Meta:
#         queryset = Calls.objects.all()
#         resource_name = 'calls'
#         filtering = {
#             'client': ALL_WITH_RELATIONS,
#         }
#         authentication = BasicAuthentication()
#         authorization = DjangoAuthorization()
#
# class ServicesResource(ModelResource):
#     calls = fields.ForeignKey(CallsResource, 'calls', null=True, blank=True)
#     staff = fields.ForeignKey(StaffResource, 'staff', null=True, blank=True)
#     safe_spaces = fields.ForeignKey(Safe_SpacesResource, 'safe_spaces', null=True, blank=True)
#     class Meta:
#         queryset = Service.objects.all()
#         resource_name = 'services'
#         authorization = DjangoAuthorization()
#         authentication = BasicAuthentication()
#
# class Police_Station_serviceResource(ModelResource):
#     services = fields.ForeignKey(ServicesResource, 'services', null=True, blank=True)
#     police_stations = fields.ForeignKey(Police_StationsResource, 'police_stations', null=True, blank=True)
#     class Meta:
#         queryset = Police_Station_service.objects.all()
#         resource_name = 'police_station_services'
#         authorization = DjangoAuthorization()
#         authentication = BasicAuthentication()
#
#
# class Health_Center_serviceResource(ModelResource):
#     services = fields.ForeignKey(ServicesResource, 'services', null=True, blank=True)
#     health_centers = fields.ForeignKey(Health_CentersResource, 'health_centers', null=True, blank=True)
#     class Meta:
#         queryset = Health_Center_service.objects.all()
#         resource_name = 'health_center_services'
#         authorization = DjangoAuthorization()
#         authentication = BasicAuthentication()