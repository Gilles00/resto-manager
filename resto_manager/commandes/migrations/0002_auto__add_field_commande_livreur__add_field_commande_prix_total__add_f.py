# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Commande.livreur'
        db.add_column(u'commandes_commande', 'livreur',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='commandes', null=True, to=orm['livreurs.Livreur']),
                      keep_default=False)

        # Adding field 'Commande.prix_total'
        db.add_column(u'commandes_commande', 'prix_total',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=2),
                      keep_default=False)

        # Adding field 'Commande.date'
        db.add_column(u'commandes_commande', 'date',
                      self.gf('django.db.models.fields.DateField')(auto_now_add=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Commande.date_acceptee'
        db.add_column(u'commandes_commande', 'date_acceptee',
                      self.gf('django.db.models.fields.DateField')(null=True),
                      keep_default=False)


        # Changing field 'LigneCommande.prix'
        db.alter_column(u'commandes_lignecommande', 'prix', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=2))

    def backwards(self, orm):
        # Deleting field 'Commande.livreur'
        db.delete_column(u'commandes_commande', 'livreur_id')

        # Deleting field 'Commande.prix_total'
        db.delete_column(u'commandes_commande', 'prix_total')

        # Deleting field 'Commande.date'
        db.delete_column(u'commandes_commande', 'date')

        # Deleting field 'Commande.date_acceptee'
        db.delete_column(u'commandes_commande', 'date_acceptee')


        # Changing field 'LigneCommande.prix'
        db.alter_column(u'commandes_lignecommande', 'prix', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2))

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
        u'commandes.commande': {
            'Meta': {'object_name': 'Commande'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'commandes'", 'to': u"orm['comptes.UserProfile']"}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'date_acceptee': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'livreur': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'commandes'", 'null': 'True', 'to': u"orm['livreurs.Livreur']"}),
            'prix_total': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2'}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'commandes'", 'to': u"orm['restaurants.Restaurant']"}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'commandes.lignecommande': {
            'Meta': {'object_name': 'LigneCommande'},
            'commande': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ligne_commandes'", 'to': u"orm['commandes.Commande']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prix': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'repas': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ligne_commandes'", 'to': u"orm['restaurants.Repas']"})
        },
        u'comptes.restaurateur': {
            'Meta': {'object_name': 'Restaurateur'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'restaurateur'", 'unique': 'True', 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'comptes.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'birthdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'user_profile'", 'unique': 'True', 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'livreurs.livreur': {
            'Meta': {'object_name': 'Livreur'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'livreur'", 'unique': 'True', 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'restaurants.menu': {
            'Meta': {'object_name': 'Menu'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'restaurant': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'menu'", 'unique': 'True', 'to': u"orm['restaurants.Restaurant']"})
        },
        u'restaurants.repas': {
            'Meta': {'object_name': 'Repas'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'repas'", 'to': u"orm['restaurants.Menu']"}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'prix': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'})
        },
        u'restaurants.restaurant': {
            'Meta': {'object_name': 'Restaurant'},
            'adresse': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'restaurateur': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'restaurants'", 'null': 'True', 'to': u"orm['comptes.Restaurateur']"}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['commandes']