from django.contrib import admin

# Register your models here.
from .models import Event, Place, City


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'city',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('event_type', 'start_date', 'place', 'capacity')
