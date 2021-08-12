from rest_framework import serializers
from apps.executors.models import Executor

class ExecutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Executor
        fields = '__all__'