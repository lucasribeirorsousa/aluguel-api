from django.urls import path, include
from rest_framework import routers

from .views import (
    AddressViewSet,
    DateViewSet,
    DaysViewSet,
    DailyCostViewSet,
    PlaceAdsViewSet,
)

router = routers.DefaultRouter()
router.register('address', AddressViewSet, basename='address')
router.register('dates', DateViewSet, basename='dates')
router.register('days', DaysViewSet, basename='days')
router.register('daily-costs', DailyCostViewSet, basename='daily-costs')
router.register('places-ads', PlaceAdsViewSet, basename='places-ads')

urlpatterns = [
    path("",  include((router.urls, 'places'), namespace='places_urls')),
]
