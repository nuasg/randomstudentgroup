# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Group.summary'
        db.add_column(u'randomgroup_group', 'summary',
                      self.gf('django.db.models.fields.TextField')(null=True),
                      keep_default=False)

        # Adding field 'Group.twitter_url'
        db.add_column(u'randomgroup_group', 'twitter_url',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Group.group_type'
        db.add_column(u'randomgroup_group', 'group_type',
                      self.gf('django.db.models.fields.TextField')(null=True),
                      keep_default=False)


        # Changing field 'Group.description'
        db.alter_column(u'randomgroup_group', 'description', self.gf('django.db.models.fields.TextField')(null=True))

    def backwards(self, orm):
        # Deleting field 'Group.summary'
        db.delete_column(u'randomgroup_group', 'summary')

        # Deleting field 'Group.twitter_url'
        db.delete_column(u'randomgroup_group', 'twitter_url')

        # Deleting field 'Group.group_type'
        db.delete_column(u'randomgroup_group', 'group_type')


        # User chose to not deal with backwards NULL issues for 'Group.description'
        raise RuntimeError("Cannot reverse this migration. 'Group.description' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Group.description'
        db.alter_column(u'randomgroup_group', 'description', self.gf('django.db.models.fields.TextField')())

    models = {
        u'randomgroup.group': {
            'Meta': {'object_name': 'Group'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'fb_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'group_type': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'p_contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'p_contact_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'twitter_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'webpage': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['randomgroup']