from rest_framework import viewsets, generics

from apps.executors.models import Executor
from apps.executors.serializers import ExecutorSerializer

class ExecutorAPIViewSet(viewsets.ModelViewSet):
    queryset = Executor.objects.all()
    serializer_class = ExecutorSerializer
