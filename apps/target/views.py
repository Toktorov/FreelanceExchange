from rest_framework import viewsets, generics
from apps.target.models import Task
from apps.target.serializers import TaskSerializer

class TaskAPIViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer