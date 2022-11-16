from rest_framework import viewsets

from .models import Asset, Banner, Spot
from .serializers import (
    AssetSerializer,
    BannerSerializer,
    SpotWithBannersSerializer,
)


class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer


class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer


class SpotViewSet(viewsets.ModelViewSet):
    queryset = Spot.objects.all()
    serializer_class = SpotWithBannersSerializer
    filterset_fields = ['location']
