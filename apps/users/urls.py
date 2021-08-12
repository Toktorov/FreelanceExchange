from rest_framework.routers import DefaultRouter
from apps.users import views
from django.urls import path

urlpatterns = [
    path('', views.ProfileAPIViewSet.as_view({'get': 'list'}), name='profile'),
]