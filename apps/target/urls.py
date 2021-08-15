from rest_framework.routers import DefaultRouter
from apps.target import views
from django.urls import path

urlpatterns = [
    path('', views.TargetAPIViewSet.as_view({'get': 'list'}), name='target'),
]