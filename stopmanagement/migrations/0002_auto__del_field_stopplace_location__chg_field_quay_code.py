# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'StopPlace.location'
        db.delete_column(u'stopmanagement_stopplace', 'location')


        # Changing field 'Quay.code'
        db.alter_column(u'stopmanagement_quay', 'code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=15))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'StopPlace.location'
        raise RuntimeError("Cannot reverse this migration. 'StopPlace.location' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'StopPlace.location'
        db.add_column(u'stopmanagement_stopplace', 'location',
                      self.gf('django.contrib.gis.db.models.fields.PointField')(),
                      keep_default=False)


        # Changing field 'Quay.code'
        db.alter_column(u'stopmanagement_quay', 'code', self.gf('django.db.models.fields.CharField')(max_length=10, unique=True))

    models = {
        u'stopmanagement.quay': {
            'Meta': {'object_name': 'Quay'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'stopplace': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stopmanagement.StopPlace']"})
        },
        u'stopmanagement.stopplace': {
            'Meta': {'object_name': 'StopPlace'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['stopmanagement']