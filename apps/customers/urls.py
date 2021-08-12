from rest_framework.routers import DefaultRouter
from apps.customers import views
from django.urls import path

urlpatterns = [
    path('', views.CustomerAPIViewSet.as_view({'get': 'list'}), name='customer'),
]