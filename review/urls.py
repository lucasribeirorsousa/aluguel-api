from django.urls import path, include
from rest_framework import routers

from .views import RatingViewSet, UserRatingsViewSet, PlaceRatingsViewSet

router = routers.DefaultRouter()
router.register('ratings', RatingViewSet, basename='ratings')
router.register('user-ratings', UserRatingsViewSet, basename='user-ratings')
router.register('place-ratings', PlaceRatingsViewSet, basename='place-ratings')

urlpatterns = [
    path("",  include((router.urls, 'review'), namespace='review_urls')),
]
