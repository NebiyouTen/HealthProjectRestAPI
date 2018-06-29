from django.conf.urls import url
from rest_framework import routers
from Registration.views import *

router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'calls', CallViewSet)
router.register(r'stafs', ClientViewSet)
router.register(r'safe_spaces', CallViewSet)
router.register(r'police_stations', ClientViewSet)
router.register(r'health_centers', CallViewSet)
router.register(r'services', ClientViewSet)
router.register(r'police_stations_services', CallViewSet)
router.register(r'health_center_services', ClientViewSet)

urlpatterns = router.urls