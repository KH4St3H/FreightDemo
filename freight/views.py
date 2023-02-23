from django.shortcuts import render
from .permissions import IsFreightCompany
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import DriverSerializer, FactorySerializer
from .models import Driver, Factory


class DriverViewSet(viewsets.ReadOnlyModelViewSet):
    """
        endpoint to list all drivers
    """
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

    permission_classes = [permissions.IsAuthenticated, IsFreightCompany]

class FactoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Factory.objects.none()
    serializer_class = FactorySerializer

    permission_classes = [permissions.IsAuthenticated, IsFreightCompany]
    
    def get_queryset(self):
        """
            returns list of associate factories of user
        """
        queryset = self.request.user.freightcompany.associate_companies.all()
        return queryset