from rest_framework import serializers
from .models import EventOrder, Cancellation, History


class EventOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventOrder
        fields = '__all__'


class CancellationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cancellation
        fields = '__all__'


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'
