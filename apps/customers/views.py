from rest_framework import viewsets, generics

from apps.customers.models import Customer
from apps.customers.serializers import CustomerSerializer

class CustomerAPIViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
