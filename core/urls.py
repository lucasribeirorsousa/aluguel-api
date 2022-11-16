from django.urls import path, include
from .views import api, public

urlpatterns = [
    path('', public, name='public'),
    path('api/', api, name='api'),
    path('api/asset/', include('asset.urls')),
    path('api/authentication/', include('authentication.urls')),
    path('api/events/', include('events.urls')),
    path('api/places/', include('places.urls')),
    path('api/review/', include('review.urls')),
    path('api/validation/', include('validation.urls')),
]
