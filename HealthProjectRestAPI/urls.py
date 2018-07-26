from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Registration.urls')),
    path('auth/', include('rest_framework_social_oauth2.urls')),
    ]
