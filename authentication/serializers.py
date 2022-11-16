from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    TokenRefreshSerializer,
)

from asset.serializers import AssetSerializer

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', )

    def to_representation(self, instance):
        self.fields['asset'] = AssetSerializer(many=False, read_only=True)
        return super().to_representation(instance)


class HintUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']


class AuthSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['id'] = user.id
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['id'] = refresh.payload['id']
        data['email'] = refresh.payload['email']
        data['username'] = self.user.username
        data['image'] = AssetSerializer(self.user.asset).data
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data["role"] = self.user.role
        return data


class RefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = RefreshToken(attrs['refresh'])
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        return data


class ChangePasswordSerializer(serializers.Serializer):
    model = User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
