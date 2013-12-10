from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from stopmanagement.models import StopPlace, Quay

admin.site.register(StopPlace, LeafletGeoAdmin)
admin.site.register(Quay, LeafletGeoAdmin)