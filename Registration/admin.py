from django.contrib import admin
from .models import *
from django.contrib.auth.models import Permission

admin.site.register(Client)
admin.site.register(Health_Centers)
admin.site.register(Police_Stations)
admin.site.register(Service)
admin.site.register(Safe_Spaces)
admin.site.register(Staff)
admin.site.register(Health_Center_service)
admin.site.register(Police_Station_service)
admin.site.register(Calls)
admin.site.register(Permission)
