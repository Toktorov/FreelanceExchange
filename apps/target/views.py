from rest_framework import viewsets, generics
from apps.target.models import Target
from apps.target.serializers import TargetSerializer

class TargetAPIViewSet(viewsets.ModelViewSet):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer