from rest_framework import viewsets, generics
from apps.users.models import Customer, Freelancer, Transaction
from apps.users.serializers import CustomerSerializer, FreelancerSerializer, TransactionSerializer

class CustomerAPIViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class FreelancerAPIViewSet(viewsets.ModelViewSet):
    queryset = Freelancer.objects.all()
    serializer_class = FreelancerSerializer

class TransactionAPIViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


