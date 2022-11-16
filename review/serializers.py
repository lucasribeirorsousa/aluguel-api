from rest_framework import serializers
from .models import Rating, UserRatings, PlaceRatings


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class UserRatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRatings
        fields = '__all__'


class PlaceRatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceRatings
        fields = '__all__'
