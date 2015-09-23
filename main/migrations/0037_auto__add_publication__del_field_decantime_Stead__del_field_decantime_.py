# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Publication'
        db.create_table(u'main_publication', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('autor', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=450)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal(u'main', ['Publication'])

        # Deleting field 'decanTime.Stead'
        db.delete_column(u'main_decantime', 'Stead')

        # Deleting field 'decanTime.Monday'
        db.delete_column(u'main_decantime', 'Monday')

        # Deleting field 'decanTime.Tuesday'
        db.delete_column(u'main_decantime', 'Tuesday')

        # Deleting field 'decanTime.Friday'
        db.delete_column(u'main_decantime', 'Friday')

        # Deleting field 'decanTime.Saturday'
        db.delete_column(u'main_decantime', 'Saturday')

        # Deleting field 'decanTime.Thursday'
        db.delete_column(u'main_decantime', 'Thursday')

        # Adding field 'decanTime.monday'
        db.add_column(u'main_decantime', 'monday',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'decanTime.tuesday'
        db.add_column(u'main_decantime', 'tuesday',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'decanTime.stead'
        db.add_column(u'main_decantime', 'stead',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'decanTime.thursday'
        db.add_column(u'main_decantime', 'thursday',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'decanTime.friday'
        db.add_column(u'main_decantime', 'friday',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'decanTime.saturday'
        db.add_column(u'main_decantime', 'saturday',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Publication'
        db.delete_table(u'main_publication')

        # Adding field 'decanTime.Stead'
        db.add_column(u'main_decantime', 'Stead',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'decanTime.Monday'
        db.add_column(u'main_decantime', 'Monday',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'decanTime.Tuesday'
        db.add_column(u'main_decantime', 'Tuesday',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'decanTime.Friday'
        db.add_column(u'main_decantime', 'Friday',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'decanTime.Saturday'
        db.add_column(u'main_decantime', 'Saturday',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'decanTime.Thursday'
        db.add_column(u'main_decantime', 'Thursday',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Deleting field 'decanTime.monday'
        db.delete_column(u'main_decantime', 'monday')

        # Deleting field 'decanTime.tuesday'
        db.delete_column(u'main_decantime', 'tuesday')

        # Deleting field 'decanTime.stead'
        db.delete_column(u'main_decantime', 'stead')

        # Deleting field 'decanTime.thursday'
        db.delete_column(u'main_decantime', 'thursday')

        # Deleting field 'decanTime.friday'
        db.delete_column(u'main_decantime', 'friday')

        # Deleting field 'decanTime.saturday'
        db.delete_column(u'main_decantime', 'saturday')


    models = {
        u'main.aboutbmstu': {
            'Meta': {'object_name': 'AboutBMSTU'},
            'article': ('sortedm2m.fields.SortedManyToManyField', [], {'to': u"orm['main.Articles']", 'symmetrical': 'False', 'blank': 'True'}),
            'facts_gallery': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['photologue.Gallery']"}),
            'facts_photo': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['photologue.Photo']"}),
            'facts_text': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
            'facts_title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'graduates': ('sortedm2m.fields.SortedManyToManyField', [], {'to': u"orm['main.Persons']", 'symmetrical': 'False', 'blank': 'True'}),
            'graduates_title': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'history_gallery': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['photologue.Gallery']"}),
            'history_photo': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['photologue.Photo']"}),
            'history_text': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
            'history_title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['photologue.Photo']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'tradition_gallery': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['photologue.Gallery']"}),
            'tradition_photo': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['photologue.Photo']"}),
            'tradition_text': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
            'tradition_title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'tree_photo': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['photologue.Photo']"}),
            'tree_title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'main.addresses': {
            'Meta': {'object_name': 'Addresses'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'main.articles': {
            'Meta': {'object_name': 'Articles'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'content': ('ckeditor.fields.RichTextField', [], {}),
            'description': ('ckeditor.fields.RichTextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isFavorite': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['photologue.Photo']"}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 6, 12, 0, 0)'}),
            'short_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'subtext': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'template': ('django.db.models.fields.CharField', [], {'default': "'base_article.html'", 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'main.banners': {
            'Meta': {'object_name': 'Banners'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['photologue.Photo']"}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'main.contacts': {
            'Meta': {'object_name': 'Contacts'},
            'addresses': ('sortedm2m.fields.SortedManyToManyField', [], {'to': u"orm['main.Addresses']", 'symmetrical': 'False', 'blank': 'True'}),
            'bank_details': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
            'contact_information': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'contactees': ('sortedm2m.fields.SortedManyToManyField', [], {'to': u"orm['main.Persons']", 'symmetrical': 'False', 'blank': 'True'}),
            'emails': ('sortedm2m.fields.SortedManyToManyField', [], {'to': u"orm['main.Emails']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone_number': ('sortedm2m.fields.SortedManyToManyField', [], {'to': u"orm['main.Phones']", 'symmetrical': 'False', 'blank': 'True'}),
            'photo_map': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['photologue.Photo']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'main.decantime': {
            'Meta': {'object_name': 'decanTime'},
            'friday': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monday': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'saturday': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'stead': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'thursday': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tuesday': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'main.departments': {
            'Meta': {'object_name': 'Departments'},
            'article': ('sortedm2m.fields.SortedManyToManyField', [], {'to': u"orm['main.Articles']", 'symmetrical': 'False', 'blank': 'True'}),
            'content': ('ckeditor.fields.RichTextField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['photologue.Photo']"}),
            'short_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'template': ('django.db.models.fields.CharField', [], {'default': "'base_department.html'", 'max_length': '50'})
        },
        u'main.emails': {
            'Meta': {'object_name': 'Emails'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'main.news': {
            'Meta': {'object_name': 'News'},
            'article': ('sortedm2m.fields.SortedManyToManyField', [], {'to': u"orm['main.Articles']", 'symmetrical': 'False', 'blank': 'True'}),
            'content': ('ckeditor.fields.RichTextField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['photologue.Gallery']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isFavorite': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['photologue.Photo']"}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 6, 12, 0, 0)'}),
            'template': ('django.db.models.fields.CharField', [], {'default': "'base_news.html'", 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'main.persons': {
            'Meta': {'object_name': 'Persons'},
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['photologue.Photo']"}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'main.phones': {
            'Meta': {'object_name': 'Phones'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'main.projects': {
            'Meta': {'object_name': 'Projects'},
            'article': ('sortedm2m.fields.SortedManyToManyField', [], {'to': u"orm['main.Articles']", 'symmetrical': 'False', 'blank': 'True'}),
            'content': ('ckeditor.fields.RichTextField', [], {}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Departments']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isFavorite': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['photologue.Photo']"}),
            'short_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'template': ('django.db.models.fields.CharField', [], {'default': "'base_project.html'", 'max_length': '50'})
        },
        u'main.publication': {
            'Meta': {'object_name': 'Publication'},
            'autor': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'content': ('django.db.models.fields.CharField', [], {'max_length': '450'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'main.units': {
            'Meta': {'object_name': 'Units'},
            'article': ('sortedm2m.fields.SortedManyToManyField', [], {'to': u"orm['main.Articles']", 'symmetrical': 'False', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['photologue.Photo']"}),
            'short_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'photologue.gallery': {
            'Meta': {'ordering': "['-date_added']", 'object_name': 'Gallery'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'photos': ('sortedm2m.fields.SortedManyToManyField', [], {'blank': 'True', 'related_name': "'galleries'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['photologue.Photo']"}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['sites.Site']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'tags': ('photologue.models.TagField', [], {'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'photologue.photo': {
            'Meta': {'ordering': "['-date_added']", 'object_name': 'Photo'},
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'crop_from': ('django.db.models.fields.CharField', [], {'default': "'center'", 'max_length': '10', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'effect': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'photo_related'", 'null': 'True', 'to': u"orm['photologue.PhotoEffect']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['sites.Site']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'tags': ('photologue.models.TagField', [], {'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            'view_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'photologue.photoeffect': {
            'Meta': {'object_name': 'PhotoEffect'},
            'background_color': ('django.db.models.fields.CharField', [], {'default': "'#FFFFFF'", 'max_length': '7'}),
            'brightness': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'color': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'contrast': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'filters': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'reflection_size': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'reflection_strength': ('django.db.models.fields.FloatField', [], {'default': '0.6'}),
            'sharpness': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'transpose_method': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['main']