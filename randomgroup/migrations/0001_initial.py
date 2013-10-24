# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Group'
        db.create_table(u'randomgroup_group', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('fb_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'randomgroup', ['Group'])

        # Adding model 'Event'
        db.create_table(u'randomgroup_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['randomgroup.Group'])),
        ))
        db.send_create_signal(u'randomgroup', ['Event'])


    def backwards(self, orm):
        # Deleting model 'Group'
        db.delete_table(u'randomgroup_group')

        # Deleting model 'Event'
        db.delete_table(u'randomgroup_event')


    models = {
        u'randomgroup.event': {
            'Meta': {'object_name': 'Event'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['randomgroup.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'randomgroup.group': {
            'Meta': {'object_name': 'Group'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'fb_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['randomgroup']