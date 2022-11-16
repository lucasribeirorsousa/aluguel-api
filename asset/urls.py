from django.urls import path, include
from rest_framework import routers

from .views import AssetViewSet, BannerViewSet, SpotViewSet

router = routers.DefaultRouter()
router.register('assets', AssetViewSet, basename='assets')
router.register('banner', BannerViewSet, basename='banner')
router.register('spot', SpotViewSet, basename='spot')

urlpatterns = [
    path("",  include((router.urls, 'asset'), namespace='asset_urls')),
]
