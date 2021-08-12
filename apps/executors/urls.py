from rest_framework.routers import DefaultRouter
from apps.executors import views
from django.urls import path

urlpatterns = [
    path('', views.ExecutorAPIViewSet.as_view({'get': 'list'}), name='executor'),
]