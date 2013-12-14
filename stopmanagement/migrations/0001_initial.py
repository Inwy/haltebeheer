# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Authority'
        db.create_table(u'stopmanagement_authority', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('authoritytype', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal(u'stopmanagement', ['Authority'])

        # Adding model 'Town'
        db.create_table(u'stopmanagement_town', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'stopmanagement', ['Town'])

        # Adding model 'HistoricalStopPlace'
        db.create_table(u'stopmanagement_historicalstopplace', (
            (u'id', self.gf('django.db.models.fields.IntegerField')(db_index=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('internalname', self.gf('django.db.models.fields.CharField')(default='Onbekend', max_length=50)),
            (u'owner_id', self.gf('django.db.models.fields.IntegerField')(db_index=True, null=True, blank=True)),
            (u'town_id', self.gf('django.db.models.fields.IntegerField')(db_index=True, null=True, blank=True)),
            ('stopplacestatus', self.gf('django.db.models.fields.CharField')(default='UNKNOWN', max_length=15)),
            ('stopplacetype', self.gf('django.db.models.fields.CharField')(default='ONSTREET', max_length=15)),
            ('added', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('changed', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            (u'changed_by_id', self.gf('django.db.models.fields.IntegerField')(db_index=True, null=True, blank=True)),
            (u'history_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            (u'history_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            (u'history_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            (u'history_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'stopmanagement', ['HistoricalStopPlace'])

        # Adding model 'StopPlace'
        db.create_table(u'stopmanagement_stopplace', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('internalname', self.gf('django.db.models.fields.CharField')(default='Onbekend', max_length=50)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stopmanagement.Authority'])),
            ('town', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stopmanagement.Town'])),
            ('stopplacestatus', self.gf('django.db.models.fields.CharField')(default='UNKNOWN', max_length=15)),
            ('stopplacetype', self.gf('django.db.models.fields.CharField')(default='ONSTREET', max_length=15)),
            ('added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('changed_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'stopmanagement', ['StopPlace'])

        # Adding model 'HistoricalQuay'
        db.create_table(u'stopmanagement_historicalquay', (
            (u'id', self.gf('django.db.models.fields.IntegerField')(db_index=True, blank=True)),
            (u'owner_id', self.gf('django.db.models.fields.IntegerField')(db_index=True, null=True, blank=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('location', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('quaystatus', self.gf('django.db.models.fields.CharField')(default='UNKNOWN', max_length=15)),
            ('quaytype', self.gf('django.db.models.fields.CharField')(default='REGULAR', max_length=15)),
            ('quaysign', self.gf('django.db.models.fields.CharField')(default='UNKNOWN', max_length=15)),
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

        # Adding model 'Quay'
        db.create_table(u'stopmanagement_quay', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stopmanagement.Authority'])),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('location', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('quaystatus', self.gf('django.db.models.fields.CharField')(default='UNKNOWN', max_length=15)),
            ('quaytype', self.gf('django.db.models.fields.CharField')(default='REGULAR', max_length=15)),
            ('quaysign', self.gf('django.db.models.fields.CharField')(default='UNKNOWN', max_length=15)),
            ('stopplace', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stopmanagement.StopPlace'])),
            ('added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('changed_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'stopmanagement', ['Quay'])

        # Adding unique constraint on 'Quay', fields ['owner', 'code']
        db.create_unique(u'stopmanagement_quay', ['owner_id', 'code'])


    def backwards(self, orm):
        # Removing unique constraint on 'Quay', fields ['owner', 'code']
        db.delete_unique(u'stopmanagement_quay', ['owner_id', 'code'])

        # Deleting model 'Authority'
        db.delete_table(u'stopmanagement_authority')

        # Deleting model 'Town'
        db.delete_table(u'stopmanagement_town')

        # Deleting model 'HistoricalStopPlace'
        db.delete_table(u'stopmanagement_historicalstopplace')

        # Deleting model 'StopPlace'
        db.delete_table(u'stopmanagement_stopplace')

        # Deleting model 'HistoricalQuay'
        db.delete_table(u'stopmanagement_historicalquay')

        # Deleting model 'Quay'
        db.delete_table(u'stopmanagement_quay')


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
        u'stopmanagement.authority': {
            'Meta': {'object_name': 'Authority'},
            'authoritytype': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'stopmanagement.historicalquay': {
            'Meta': {'ordering': "(u'-history_date', u'-history_id')", 'object_name': 'HistoricalQuay'},
            'added': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'changed': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            u'changed_by_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            u'history_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'history_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'history_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'history_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            u'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'owner_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'quaysign': ('django.db.models.fields.CharField', [], {'default': "'UNKNOWN'", 'max_length': '15'}),
            'quaystatus': ('django.db.models.fields.CharField', [], {'default': "'UNKNOWN'", 'max_length': '15'}),
            'quaytype': ('django.db.models.fields.CharField', [], {'default': "'REGULAR'", 'max_length': '15'}),
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
            'internalname': ('django.db.models.fields.CharField', [], {'default': "'Onbekend'", 'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'owner_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'stopplacestatus': ('django.db.models.fields.CharField', [], {'default': "'UNKNOWN'", 'max_length': '15'}),
            'stopplacetype': ('django.db.models.fields.CharField', [], {'default': "'ONSTREET'", 'max_length': '15'}),
            u'town_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'stopmanagement.quay': {
            'Meta': {'unique_together': "(('owner', 'code'),)", 'object_name': 'Quay'},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'changed_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stopmanagement.Authority']"}),
            'quaysign': ('django.db.models.fields.CharField', [], {'default': "'UNKNOWN'", 'max_length': '15'}),
            'quaystatus': ('django.db.models.fields.CharField', [], {'default': "'UNKNOWN'", 'max_length': '15'}),
            'quaytype': ('django.db.models.fields.CharField', [], {'default': "'REGULAR'", 'max_length': '15'}),
            'stopplace': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stopmanagement.StopPlace']"})
        },
        u'stopmanagement.stopplace': {
            'Meta': {'object_name': 'StopPlace'},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'changed_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internalname': ('django.db.models.fields.CharField', [], {'default': "'Onbekend'", 'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stopmanagement.Authority']"}),
            'stopplacestatus': ('django.db.models.fields.CharField', [], {'default': "'UNKNOWN'", 'max_length': '15'}),
            'stopplacetype': ('django.db.models.fields.CharField', [], {'default': "'ONSTREET'", 'max_length': '15'}),
            'town': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stopmanagement.Town']"})
        },
        u'stopmanagement.town': {
            'Meta': {'object_name': 'Town'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['stopmanagement']