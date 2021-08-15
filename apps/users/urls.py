from rest_framework.routers import DefaultRouter
from apps.users import views
from django.urls import path

router = DefaultRouter()
router.register('customer', views.CustomerAPIViewSet, basename='customer')
router.register('freelancer', views.FreelancerAPIViewSet, basename='freelancer')
router.register('transactions', views.TransactionAPIViewSet, basename='transaction')

urlpatterns = router.urls