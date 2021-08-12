from rest_framework.routers import DefaultRouter
from apps.target import views
from django.urls import path

urlpatterns = [
    path('', views.TaskAPIViewSet.as_view({'get': 'list'}), name='task'),
]