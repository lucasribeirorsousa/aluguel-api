from django.urls import path, include
from rest_framework import routers

from .views import ValidationViewSet
router = routers.DefaultRouter()
router.register('validations', ValidationViewSet, basename='validations')

urlpatterns = [
    path("",  include((router.urls, 'validation'), namespace='validation_urls')),
]
