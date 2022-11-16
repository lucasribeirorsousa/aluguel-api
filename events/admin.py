from django.contrib import admin
from .models import EventOrder, Cancellation, History

# Register your models here.
admin.site.register(EventOrder)
admin.site.register(Cancellation)
admin.site.register(History)
