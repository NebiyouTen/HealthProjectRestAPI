from .resource import *
from tastypie.api import Api
from django.conf.urls import url, include


health_api = Api(api_name='v1')

health_api.register(Safe_SpacesResource())

health_api.register(Health_CentersResource())
health_api.register(Police_StationsResource())
health_api.register(ClientsResource())

health_api.register(CallsResource())



health_api.register(StaffResource())



health_api.register(ServicesResource())
health_api.register(Police_Station_serviceResource())
health_api.register(Health_Center_serviceResource())


urlpatterns = [
    url('', include(health_api.urls)),
]