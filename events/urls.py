from django.urls import path, include
from rest_framework import routers

from .views import EventOrderViewSet, CancellationViewSet, HistoryViewSet

router = routers.DefaultRouter()
router.register('event-orders', EventOrderViewSet, basename='event-orders')
router.register('event-histories', HistoryViewSet, basename='event-histories')
router.register('cancellations', CancellationViewSet, basename='cancellations')

urlpatterns = [
    path("",  include((router.urls, 'events'), namespace='events_urls')),
]
