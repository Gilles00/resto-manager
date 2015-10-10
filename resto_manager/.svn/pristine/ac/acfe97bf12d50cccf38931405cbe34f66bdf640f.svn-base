#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	
	url(r'^passer-commande/$','commandes.views.passer_commande'),
	url(r'^add_repas/([0-9]*)','commandes.views.add_repas_to_commande'),
	url(r'^get/([0-9]*)', 'commandes.views.get_session_commande'),
	url(r'^get_confirm_commande_message/([0-9]*)', 'commandes.views.get_confirm_commande_message'),
	url(r'^confirm_commande/([0-9]*)', 'commandes.views.confirm_commande'),
	url(r'^mes_commandes/', 'commandes.views.mes_commandes'),
	url(r'^get_commandes_by_restaurant/([0-9]*)', 'commandes.views.get_commandes_by_restaurant'),
	url(r'^preparer_commande/([0-9]*)', 'commandes.views.preparer_commande'),
	url(r'^terminer_commande/([0-9]*)', 'commandes.views.terminer_commande'),
	url(r'^choisir_commande/([0-9]*)', 'commandes.views.choisir_commande'),
	url(r'^livrer_commande/([0-9]*)', 'commandes.views.livrer_commande'),
)
