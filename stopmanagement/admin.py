from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from stopmanagement.models import StopPlace, Quay, Town, Authority

admin.site.register(StopPlace, LeafletGeoAdmin)
admin.site.register(Quay, LeafletGeoAdmin)
admin.site.register(Town)
admin.site.register(Authority)