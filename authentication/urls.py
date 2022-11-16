from django.urls import path, include
from rest_framework import routers

from .views import (
    ChangePasswordViewSet,
    UserViewSet,
    AuthViewSet,
    RefreshViewSet,
)

router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path(
        "",
        include(
            (router.urls, 'authentication'),
            namespace='authentication_urls',
        ),
    ),
    path('login/', AuthViewSet.as_view(), name='login'),
    path('refresh/', RefreshViewSet.as_view(), name='refresh'),
    path(
        'change-password/',
        ChangePasswordViewSet.as_view(),
        name='change-password',
    ),
    path(
        'reset-password/',
        include('django_rest_passwordreset.urls', namespace='reset-password'),
    ),
]
