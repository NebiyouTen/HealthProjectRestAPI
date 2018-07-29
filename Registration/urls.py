from django.conf.urls import url
from rest_framework import routers
from Registration.views import *

router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'calls', CallViewSet)
router.register(r'staffs', StaffViewSet)
router.register(r'safe_spaces', Safe_SpacesViewSet)
router.register(r'police_stations', Police_StationsViewSet)
router.register(r'health_centers', Health_CentersViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'police_station_services', Police_Station_serviceViewSet)
router.register(r'health_center_services', Health_Center_serviceViewSet)
router.register(r'automated_call', Automated_callViewSet)

urlpatterns = router.urls
