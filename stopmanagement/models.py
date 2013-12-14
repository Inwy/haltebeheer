from django.contrib.gis.db import models
from simple_history.models import HistoricalRecords
from django.utils.translation import ugettext, ugettext_lazy as _
from stopmanagement.enum import *

class Authority(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    authoritytype = models.CharField(max_length=3, choices=AUTHORITYTYPE)

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.code)

    class Meta:
        verbose_name = _("authority")
        verbose_name_plural = _("authorities")

class Town(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.code)

    class Meta:
        verbose_name = _("town")
        verbose_name_plural = _("towns")

class StopPlace(models.Model):
    name = models.CharField(max_length=50)
    internalname = models.CharField(max_length=50, default='Onbekend')
    owner = models.ForeignKey('Authority')
    town = models.ForeignKey('Town')
    stopplacestatus = models.CharField(max_length=15, choices=STOPPLACESTATUS, default='UNKNOWN')
    stopplacetype = models.CharField(max_length=15, choices=STOPPLACETYPE, default='ONSTREET')

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

    def __unicode__(self):
        return "%s - %s" % (self.name, self.town)

    class Meta:
        verbose_name = _("stopplace")
        verbose_name_plural = _("stopplaces")

    pass

class Quay(models.Model):
    owner = models.ForeignKey('Authority')
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=50)
    location = models.PointField()

    quaystatus = models.CharField(max_length=15, choices=QUAYSTATUS, default='UNKNOWN')
    quaytype = models.CharField(max_length=15, choices=QUAYTYPE, default='REGULAR')
    quaysign = models.CharField(max_length=15, choices=QUAYSIGN, default='UNKNOWN')

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

    def __unicode__(self):
        return "%s (%s%s)" % (self.name, self.owner.code, self.code)

    class Meta:
        verbose_name = _("quay")
        verbose_name_plural = _("quays")
        unique_together = ('owner', 'code')
