from django.shortcuts import render
from .permissions import IsFreightCompany
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import DriverSerializer
from .models import Driver


class DriverViewSet(viewsets.ModelViewSet):
    """
        endpoint to list all drivers
    """
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

    permission_classes = [permissions.IsAuthenticated, IsFreightCompany]