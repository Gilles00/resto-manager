#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.db.models.signals import post_save
import reversion

# Create your models here.

class Restaurant(models.Model):
    restaurateur = models.ForeignKey('comptes.Restaurateur', related_name='restaurants', null=True)
    nom = models.CharField(max_length=30, null=True)
    adresse = models.CharField(max_length=100, null=True, blank=True)
    telephone = models.CharField(max_length=30, null=True, blank=True)

    def __unicode__(self):
        return self.nom

#Pour le undo
reversion.register(Restaurant)

class Menu(models.Model):
	nom = models.CharField(max_length=50, null=True, verbose_name='Nom du menu')
	restaurant = models.OneToOneField("Restaurant", related_name='menu')

	def __unicode__(self):
		return self.nom

class Repas(models.Model):
	nom = models.CharField(max_length=50, verbose_name='Nom du repas')
	description = models.TextField(max_length=50)
	prix = models.DecimalField(max_digits=8, decimal_places=2)
	menu = models.ForeignKey("Menu", related_name='repas')

	def __unicode__(self):
		return self.nom

"""
Chaque fois qu'un restaurant est créé, on lui attribue un menu
"""
def bind_with_menu(sender, instance, created, **kwargs):
    if created:
        instance.menu = Menu()
        instance.menu.save()
post_save.connect(bind_with_menu, sender=Restaurant)