from rest_framework import viewsets

from .models import EventOrder, Cancellation, History
from .serializers import (
    EventOrderSerializer,
    CancellationSerializer,
    HistorySerializer,
)


class EventOrderViewSet(viewsets.ModelViewSet):
    queryset = EventOrder.objects.all()
    serializer_class = EventOrderSerializer


class CancellationViewSet(viewsets.ModelViewSet):
    queryset = Cancellation.objects.all()
    serializer_class = CancellationSerializer


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
