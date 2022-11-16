from .serializers import (
    UserSerializer,
    ChangePasswordSerializer,
    AuthSerializer,
    RefreshSerializer,
)
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework.permissions import IsAuthenticated

from .models import User
from .permissions import UserPermissions


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermissions]


class AuthViewSet(TokenViewBase):
    serializer_class = AuthSerializer


class RefreshViewSet(TokenViewBase):
    serializer_class = RefreshSerializer


class ChangePasswordViewSet(UpdateAPIView):
    model = User
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self, queryset=None):
        return User.objects.get(id=self.request.user.id)

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            check = user.check_password(
                serializer.data.get("old_password")
            )

            if not check:
                return Response(
                    {"old_password": "Senha errada."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            user.password = serializer.data.get("new_password")
            user.save()

            return Response(None, status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
