from django.contrib.gis.db import models
from simple_history.models import HistoricalRecords
from django.utils.translation import ugettext, ugettext_lazy as _

class StopPlace(models.Model):
    name = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    region = models.CharField(max_length=50)

    objects = models.GeoManager()
    added = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)
    changed_by = models.ForeignKey('auth.User')
    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user_setter(self, value):
        self.changed_by = value


    class Meta:
            verbose_name = _("stopplace")
            verbose_name_plural = _("stopplaces")

    pass

class Quay(models.Model):
    code = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=50)
    location = models.PointField()

    stopplace = models.ForeignKey('StopPlace')

    objects = models.GeoManager()
    added = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)
    changed_by = models.ForeignKey('auth.User')
    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user_setter(self, value):
        self.changed_by = value

    class Meta:
            verbose_name = _("quay")
            verbose_name_plural = _("quays")
