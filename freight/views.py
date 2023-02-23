from django.shortcuts import render
from .permissions import IsFreightCompany, IsFactory
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import DriverSerializer, FactorySerializer, LoadSerializer
from .models import Driver, Factory, Load


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

class LoadViewSet(viewsets.ModelViewSet):
    queryset = Load.objects.none()
    serializer_class = LoadSerializer

    permission_classes = [permissions.IsAuthenticated, IsFreightCompany|IsFactory]

    def get_queryset(self):
        queryset = Load.objects.none()
        try:
            queryset = self.request.user.factory.load_set.all()
        except:
            freight_company = self.request.user.freightcompany
            queryset = Load.objects.filter(factory__in=freight_company.associate_companies.all(), status='accepting')
        return queryset