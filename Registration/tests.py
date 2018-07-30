from django.test import TestCase
from datetime import datetime
from .models import *
from .serializers import *
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from django.shortcuts import reverse
from rest_framework import status

# client = APIClient()
# Create your tests here.
class GetAllCallsTest(APITestCase):

    def test_get_all_calls(self):
        client = APIClient()
        url = '/api/calls/'
        response = client.get(url)
        calls = Calls.objects.all()
        serializer = CallsSerializer(calls, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetAllServicesTest(TestCase):

    def test_get_all_s(self):
        client = APIClient()
        respone = client.get('/api/services/')
        services = Services.objects.all()
        serializer = ServiceSerializer(calls, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
