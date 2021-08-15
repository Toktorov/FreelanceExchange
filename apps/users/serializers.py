from rest_framework import serializers
from apps.users.models import Customer, Freelancer, Transaction

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class FreelancerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Freelancer
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'