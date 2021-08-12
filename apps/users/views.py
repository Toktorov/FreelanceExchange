from rest_framework import viewsets, generics
from apps.users.models import Profile
from apps.users.serializers import ProfileSerializer

class ProfileAPIViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer