from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include


urlpatterns = [
    path('admin/', admin.site.urls),

    # path('users/', admin.site.urls),

    path('api/', include('Registration.urls')),
    # url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('auth/', include('rest_framework_social_oauth2.urls')),
    ]
