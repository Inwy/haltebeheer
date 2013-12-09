from django.contrib.gis.db import models
from django.utils.translation import ugettext, ugettext_lazy as _

class StopPlace(models.Model):
    name = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    location = models.PointField()

    objects = models.GeoManager()

    class Meta:
            verbose_name = _("stopplace")
            verbose_name_plural = _("stopplaces")

    pass

class Quay(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50)
    location = models.PointField()

    stopplace = models.ForeignKey('StopPlace')

    objects = models.GeoManager()

    class Meta:
            verbose_name = _("quay")
            verbose_name_plural = _("quays")
