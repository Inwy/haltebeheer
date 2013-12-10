# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HistoricalQuay'
        db.create_table(u'stopmanagement_historicalquay', (
            (u'id', self.gf('django.db.models.fields.IntegerField')(db_index=True, blank=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('location', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            (u'stopplace_id', self.gf('django.db.models.fields.IntegerField')(db_index=True, null=True, blank=True)),
            ('added', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('changed', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            (u'changed_by_id', self.gf('django.db.models.fields.IntegerField')(db_index=True, null=True, blank=True)),
            (u'history_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            (u'history_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            (u'history_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            (u'history_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'stopmanagement', ['HistoricalQuay'])

        # Adding model 'HistoricalStopPlace'
        db.create_table(u'stopmanagement_historicalstopplace', (
            (u'id', self.gf('django.db.models.fields.IntegerField')(db_index=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('owner', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('added', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('changed', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            (u'changed_by_id', self.gf('django.db.models.fields.IntegerField')(db_index=True, null=True, blank=True)),
            (u'history_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            (u'history_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            (u'history_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            (u'history_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'stopmanagement', ['HistoricalStopPlace'])

        # Adding field 'StopPlace.added'
        db.add_column(u'stopmanagement_stopplace', 'added',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 12, 11, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'StopPlace.changed'
        db.add_column(u'stopmanagement_stopplace', 'changed',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 12, 11, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'StopPlace.changed_by'
        db.add_column(u'stopmanagement_stopplace', 'changed_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'Quay.added'
        db.add_column(u'stopmanagement_quay', 'added',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 12, 11, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Quay.changed'
        db.add_column(u'stopmanagement_quay', 'changed',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 12, 11, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Quay.changed_by'
        db.add_column(u'stopmanagement_quay', 'changed_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['auth.User']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'HistoricalQuay'
        db.delete_table(u'stopmanagement_historicalquay')

        # Deleting model 'HistoricalStopPlace'
        db.delete_table(u'stopmanagement_historicalstopplace')

        # Deleting field 'StopPlace.added'
        db.delete_column(u'stopmanagement_stopplace', 'added')

        # Deleting field 'StopPlace.changed'
        db.delete_column(u'stopmanagement_stopplace', 'changed')

        # Deleting field 'StopPlace.changed_by'
        db.delete_column(u'stopmanagement_stopplace', 'changed_by_id')

        # Deleting field 'Quay.added'
        db.delete_column(u'stopmanagement_quay', 'added')

        # Deleting field 'Quay.changed'
        db.delete_column(u'stopmanagement_quay', 'changed')

        # Deleting field 'Quay.changed_by'
        db.delete_column(u'stopmanagement_quay', 'changed_by_id')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'stopmanagement.historicalquay': {
            'Meta': {'ordering': "(u'-history_date', u'-history_id')", 'object_name': 'HistoricalQuay'},
            'added': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'changed': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            u'changed_by_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            u'history_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'history_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'history_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'history_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            u'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'stopplace_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'stopmanagement.historicalstopplace': {
            'Meta': {'ordering': "(u'-history_date', u'-history_id')", 'object_name': 'HistoricalStopPlace'},
            'added': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'changed': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            u'changed_by_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            u'history_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'history_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'history_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'history_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            u'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'stopmanagement.quay': {
            'Meta': {'object_name': 'Quay'},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'changed_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'stopplace': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stopmanagement.StopPlace']"})
        },
        u'stopmanagement.stopplace': {
            'Meta': {'object_name': 'StopPlace'},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'changed_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['stopmanagement']