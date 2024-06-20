from django.contrib import admin
from .models import Locations, Trips


class LocationsAdmin(admin.ModelAdmin):
    list_display = ("id", "location_area", "location_name", "embarcation_text", "type")

# Register your models here.
admin.site.register(Locations, LocationsAdmin)
admin.site.register(Trips)