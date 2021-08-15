from rest_framework import serializers
from apps.target.models import Target

class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = '__all__'