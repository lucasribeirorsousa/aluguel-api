from rest_framework import serializers
from .models import (
    Address,
    Date,
    Days,
    DailyCost,
    PlaceAds,
)


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Date
        fields = '__all__'


class DaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Days
        fields = '__all__'


class DailyCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyCost
        fields = '__all__'


class PlaceAdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceAds
        fields = '__all__'
