# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Type'
        db.create_table('characters_type', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=16)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('characters', ['Type'])

        # Adding model 'Level'
        db.create_table('characters_level', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=16)),
            ('xp', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, max_length=16)),
        ))
        db.send_create_signal('characters', ['Level'])

        # Adding model 'Character'
        db.create_table('characters_character', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=16, db_index=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['characters.Type'])),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(default=1, max_length=10)),
            ('xp', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, max_length=16)),
        ))
        db.send_create_signal('characters', ['Character'])


    def backwards(self, orm):
        # Deleting model 'Type'
        db.delete_table('characters_type')

        # Deleting model 'Level'
        db.delete_table('characters_level')

        # Deleting model 'Character'
        db.delete_table('characters_character')


    models = {
        'characters.character': {
            'Meta': {'object_name': 'Character'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'max_length': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '16', 'db_index': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['characters.Type']"}),
            'xp': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'max_length': '16'})
        },
        'characters.level': {
            'Meta': {'object_name': 'Level'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '16'}),
            'xp': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'max_length': '16'})
        },
        'characters.type': {
            'Meta': {'object_name': 'Type'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '16'})
        }
    }

    complete_apps = ['characters']