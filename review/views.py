from rest_framework import viewsets

from .models import Rating, UserRatings, PlaceRatings
from .serializers import (
    RatingSerializer,
    UserRatingsSerializer,
    PlaceRatingsSerializer,
)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class UserRatingsViewSet(viewsets.ModelViewSet):
    queryset = UserRatings.objects.all()
    serializer_class = UserRatingsSerializer


class PlaceRatingsViewSet(viewsets.ModelViewSet):
    queryset = PlaceRatings.objects.all()
    serializer_class = PlaceRatingsSerializer
