# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Group.is_active'
        db.add_column(u'randomgroup_group', 'is_active',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Group.is_active'
        db.delete_column(u'randomgroup_group', 'is_active')


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
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['randomgroup']