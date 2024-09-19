from django.contrib import admin
from .models import User, Locations, Trips, Spot_Bookings, Messages, FAQ


class LocationsAdmin(admin.ModelAdmin):
    list_display = ("id", "location_area", "location_name", "embarcation_text", "type")

# Register your models here.
admin.site.register(Locations, LocationsAdmin)
admin.site.register(Trips)
admin.site.register(Spot_Bookings)
admin.site.register(Messages)
admin.site.register(FAQ)
admin.site.register(User)