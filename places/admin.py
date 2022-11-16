from django.contrib import admin
from .models import Address, Date, Days, DailyCost, PlaceAds

# Register your models here.
admin.site.register(Address)
admin.site.register(Date)
admin.site.register(Days)
admin.site.register(DailyCost)
admin.site.register(PlaceAds)
