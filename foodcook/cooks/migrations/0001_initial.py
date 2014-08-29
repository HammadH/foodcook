# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Area'
        db.create_table(u'cooks_area', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'cooks', ['Area'])

        # Adding model 'Cuisines'
        db.create_table(u'cooks_cuisines', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'cooks', ['Cuisines'])

        # Adding model 'Cook'
        db.create_table(u'cooks_cook', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], unique=True)),
            ('image', self.gf(u'sorl.thumbnail.fields.ImageField')(default='cooks/static/default/profile.png', max_length=100, blank=True)),
            ('mobile', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('intro', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('breakfast', self.gf('django.db.models.fields.BooleanField')()),
            ('lunch', self.gf('django.db.models.fields.BooleanField')()),
            ('dinner', self.gf('django.db.models.fields.BooleanField')()),
            ('price_regular', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('price_special', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('area_info', self.gf('django.db.models.fields.CharField')(max_length=70, blank=True)),
            ('is_regular', self.gf('django.db.models.fields.BooleanField')()),
            ('is_special', self.gf('django.db.models.fields.BooleanField')()),
            ('will_bring_grocery', self.gf('django.db.models.fields.BooleanField')()),
            ('can_come_home', self.gf('django.db.models.fields.BooleanField')()),
            ('has_delivery', self.gf('django.db.models.fields.BooleanField')()),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'cooks', ['Cook'])

        # Adding M2M table for field areas on 'Cook'
        m2m_table_name = db.shorten_name(u'cooks_cook_areas')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cook', models.ForeignKey(orm[u'cooks.cook'], null=False)),
            ('area', models.ForeignKey(orm[u'cooks.area'], null=False))
        ))
        db.create_unique(m2m_table_name, ['cook_id', 'area_id'])

        # Adding M2M table for field cuisines on 'Cook'
        m2m_table_name = db.shorten_name(u'cooks_cook_cuisines')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cook', models.ForeignKey(orm[u'cooks.cook'], null=False)),
            ('cuisines', models.ForeignKey(orm[u'cooks.cuisines'], null=False))
        ))
        db.create_unique(m2m_table_name, ['cook_id', 'cuisines_id'])

        # Adding model 'Meal'
        db.create_table(u'cooks_meal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('image', self.gf(u'sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('cook', self.gf('django.db.models.fields.related.ForeignKey')(related_name='meals', to=orm['cooks.Cook'])),
        ))
        db.send_create_signal(u'cooks', ['Meal'])


    def backwards(self, orm):
        # Deleting model 'Area'
        db.delete_table(u'cooks_area')

        # Deleting model 'Cuisines'
        db.delete_table(u'cooks_cuisines')

        # Deleting model 'Cook'
        db.delete_table(u'cooks_cook')

        # Removing M2M table for field areas on 'Cook'
        db.delete_table(db.shorten_name(u'cooks_cook_areas'))

        # Removing M2M table for field cuisines on 'Cook'
        db.delete_table(db.shorten_name(u'cooks_cook_cuisines'))

        # Deleting model 'Meal'
        db.delete_table(u'cooks_meal')


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
            'area_info': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'areas': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['cooks.Area']", 'symmetrical': 'False'}),
            'breakfast': ('django.db.models.fields.BooleanField', [], {}),
            'can_come_home': ('django.db.models.fields.BooleanField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'cuisines': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['cooks.Cuisines']", 'symmetrical': 'False'}),
            'dinner': ('django.db.models.fields.BooleanField', [], {}),
            'has_delivery': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': (u'sorl.thumbnail.fields.ImageField', [], {'default': "'cooks/static/default/profile.png'", 'max_length': '100', 'blank': 'True'}),
            'intro': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'is_regular': ('django.db.models.fields.BooleanField', [], {}),
            'is_special': ('django.db.models.fields.BooleanField', [], {}),
            'lunch': ('django.db.models.fields.BooleanField', [], {}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'price_regular': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'price_special': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'will_bring_grocery': ('django.db.models.fields.BooleanField', [], {})
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