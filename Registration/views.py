from rest_framework import viewsets
from Registration.serializers import *
from Registration.models import *
from Registration.permission import IsAuthenticatedOrCreate

class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer


class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer

class SectorViewSet(viewsets.ModelViewSet):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (IsAuthenticatedOrCreate,)

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticatedOrCreate,)

class CallViewSet(viewsets.ModelViewSet):
    queryset = Calls.objects.all()
    serializer_class = CallsSerializer

    def get_queryset(self):
        query_set = Calls.objects.all()
        phone_number = self.request.query_params.get('phone_number', None)
        if phone_number is not None:
            query_set = query_set.filter(phone_number=phone_number)

        return query_set
    # permission_classes = (IsAuthenticatedOrCreate,)


class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = (IsAuthenticatedOrCreate,)

class Safe_SpacesViewSet(viewsets.ModelViewSet):
    queryset = Safe_Spaces.objects.all()
    serializer_class = Safe_SpacesSerializer
    permission_classes = (IsAuthenticatedOrCreate,)

class Police_StationsViewSet(viewsets.ModelViewSet):
    queryset = Police_Stations.objects.all()
    serializer_class = Police_StationsSerializer
    permission_classes = (IsAuthenticatedOrCreate,)

class Health_CentersViewSet(viewsets.ModelViewSet):
    queryset = Health_Centers.objects.all()
    serializer_class = Health_CentersSerializer
    permission_classes = (IsAuthenticatedOrCreate,)

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (IsAuthenticatedOrCreate,)

class Police_Station_serviceViewSet(viewsets.ModelViewSet):
    queryset = Police_Station_service.objects.all()
    serializer_class = Police_Station_serviceSerializer
    permission_classes = (IsAuthenticatedOrCreate,)


class Health_Center_serviceViewSet(viewsets.ModelViewSet):
    queryset = Health_Center_service.objects.all()
    serializer_class = Health_Center_serviceSerializer
    permission_classes = (IsAuthenticatedOrCreate,)

class Automated_callViewSet(viewsets.ModelViewSet):
    queryset = Automated_call.objects.all()
    serializer_class = Automated_callSerializer
    permission_classes = (IsAuthenticatedOrCreate,)
