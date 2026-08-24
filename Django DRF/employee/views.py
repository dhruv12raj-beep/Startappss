from django.shortcuts import render
from rest_framework import viewsets
from .models import  Employee
from .serializers import EmployeeSerializer
from .permissions import IsAdminOrReadOnly
from rest_framework.permissions import AllowAny
from .throttles import EmpoloyeeRateThrottle    

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdminOrReadOnly]
    throttle_classes = [EmpoloyeeRateThrottle]

# viewset: viewset is a class that groups
# related API operations such as list, create, retreive, update, delete into a single class
# router: router automatically generates URL patterns for viewsets 