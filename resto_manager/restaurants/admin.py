#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib import messages
from restaurants.models import Restaurant, Menu, Repas

# Register your models here.

class RestaurantAdmin(admin.ModelAdmin):

    list_display = ('nom', 'adresse', 'restaurateur')

    def save_model(self, request, obj, form, change):

        print vars(form).keys()
        print form.cleaned_data

        if form.cleaned_data['restaurateur'] is None:
            print 'Il est none'
            messages.add_message(request, messages.INFO, u'Aucun Restaurateur n\'a été attribué au restaurant.')
        super(RestaurantAdmin, self).save_model(request, obj, form, change)

class RepasAdmin(admin.TabularInline):
    model = Repas
    extra = 0

class MenuAdmin(admin.ModelAdmin):
	model = Menu
	inlines = [RepasAdmin]

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Menu, MenuAdmin)