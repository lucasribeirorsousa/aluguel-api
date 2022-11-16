from django.utils import timezone
from django.forms.models import model_to_dict
from rest_framework import serializers
from .models import Asset, Banner, Spot


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'


class BannerSerializer(serializers.ModelSerializer):
    asset = serializers.FileField(write_only=True)

    class Meta:
        model = Banner
        fields = '__all__'

    def create(self, body):
        try:
            file = body['asset']
            hyperlink = body['hyperlink']
            asset = Asset.objects.create(
                file_high=file, type=1
            )
            banner = Banner.objects.create(
                hyperlink=hyperlink, asset=asset
            )
            return banner
        except Exception:
            pass

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'hyperlink': instance.hyperlink,
            'expires': instance.expires,
            'description': instance.description,
            'spot': SpotSerializer(instance=instance.spot).data,
            'asset': AssetSerializer(instance=instance.asset).data
        }


class SpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spot
        fields = '__all__'


class SpotWithBannersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spot
        fields = '__all__'

    def to_representation(self, instance):
        data = []
        banners = Banner.objects.filter(
            spot=instance, expires__gt=timezone.now())

        for i, banner in enumerate(banners):
            data.append(model_to_dict(banner))
            data[i]['asset'] = AssetSerializer(instance=banner.asset).data

        return {
            'id': instance.id,
            'description': instance.description,
            'location': instance.location,
            'created_at': instance.created_at,
            'banners': data
        }
