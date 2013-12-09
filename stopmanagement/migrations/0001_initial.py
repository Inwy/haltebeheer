# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'StopPlace'
        db.create_table(u'stopmanagement_stopplace', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('owner', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('location', self.gf('django.contrib.gis.db.models.fields.PointField')()),
        ))
        db.send_create_signal(u'stopmanagement', ['StopPlace'])

        # Adding model 'Quay'
        db.create_table(u'stopmanagement_quay', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('location', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('stopplace', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stopmanagement.StopPlace'])),
        ))
        db.send_create_signal(u'stopmanagement', ['Quay'])


    def backwards(self, orm):
        # Deleting model 'StopPlace'
        db.delete_table(u'stopmanagement_stopplace')

        # Deleting model 'Quay'
        db.delete_table(u'stopmanagement_quay')


    models = {
        u'stopmanagement.quay': {
            'Meta': {'object_name': 'Quay'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'stopplace': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stopmanagement.StopPlace']"})
        },
        u'stopmanagement.stopplace': {
            'Meta': {'object_name': 'StopPlace'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['stopmanagement']