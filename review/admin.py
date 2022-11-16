from django.contrib import admin
from .models import Rating, UserRatings, PlaceRatings

# Register your models here.
admin.site.register(Rating)
admin.site.register(UserRatings)
admin.site.register(PlaceRatings)
