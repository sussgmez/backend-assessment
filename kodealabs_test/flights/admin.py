from django.contrib import admin
from .models import Itinerarie, Leg


@admin.register(Itinerarie)
class ItinerariesAdmin(admin.ModelAdmin):
    pass


@admin.register(Leg)
class LegAdmin(admin.ModelAdmin):
    pass

