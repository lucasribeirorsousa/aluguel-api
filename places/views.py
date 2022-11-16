from rest_framework import viewsets

from .models import (
    Address,
    Date,
    Days,
    DailyCost,
    PlaceAds,
)
from .serializers import (
    AddressSerializer,
    DateSerializer,
    DaysSerializer,
    DailyCostSerializer,
    PlaceAdsSerializer,
)


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class DateViewSet(viewsets.ModelViewSet):
    queryset = Date.objects.all()
    serializer_class = DateSerializer


class DaysViewSet(viewsets.ModelViewSet):
    queryset = Days.objects.all()
    serializer_class = DaysSerializer


class DailyCostViewSet(viewsets.ModelViewSet):
    queryset = DailyCost.objects.all()
    serializer_class = DailyCostSerializer


class PlaceAdsViewSet(viewsets.ModelViewSet):
    queryset = PlaceAds.objects.all()
    serializer_class = PlaceAdsSerializer
