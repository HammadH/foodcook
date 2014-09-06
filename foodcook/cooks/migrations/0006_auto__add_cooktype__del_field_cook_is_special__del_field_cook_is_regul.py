# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CookType'
        db.create_table(u'cooks_cooktype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'cooks', ['CookType'])

        # Deleting field 'Cook.is_special'
        db.delete_column(u'cooks_cook', 'is_special')

        # Deleting field 'Cook.is_regular'
        db.delete_column(u'cooks_cook', 'is_regular')

        # Adding field 'Cook.cook_type'
        db.add_column(u'cooks_cook', 'cook_type',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cooks.CookType'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'CookType'
        db.delete_table(u'cooks_cooktype')


        # User chose to not deal with backwards NULL issues for 'Cook.is_special'
        raise RuntimeError("Cannot reverse this migration. 'Cook.is_special' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Cook.is_special'
        db.add_column(u'cooks_cook', 'is_special',
                      self.gf('django.db.models.fields.BooleanField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Cook.is_regular'
        raise RuntimeError("Cannot reverse this migration. 'Cook.is_regular' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Cook.is_regular'
        db.add_column(u'cooks_cook', 'is_regular',
                      self.gf('django.db.models.fields.BooleanField')(),
                      keep_default=False)

        # Deleting field 'Cook.cook_type'
        db.delete_column(u'cooks_cook', 'cook_type_id')


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
        u'cooks.area': {
            'Meta': {'object_name': 'Area'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'cooks.cook': {
            'Meta': {'object_name': 'Cook'},
            'area_info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'areas': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['cooks.Area']", 'symmetrical': 'False'}),
            'breakfast': ('django.db.models.fields.BooleanField', [], {}),
            'cook_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cooks.CookType']", 'null': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'cuisines': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['cooks.Cuisines']", 'symmetrical': 'False'}),
            'dinner': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': (u'sorl.thumbnail.fields.ImageField', [], {'default': "'/home/dubizzle/projects/foodcook/foodcook/foodcook/media/default/profile1.png'", 'max_length': '100', 'blank': 'True'}),
            'intro': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'lunch': ('django.db.models.fields.BooleanField', [], {}),
            'max_price': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'min_price': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'cooks.cooktype': {
            'Meta': {'object_name': 'CookType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'cooks.cuisines': {
            'Meta': {'object_name': 'Cuisines'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'cooks.meal': {
            'Meta': {'object_name': 'Meal'},
            'cook': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'meals'", 'to': u"orm['cooks.Cook']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': (u'sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['cooks']