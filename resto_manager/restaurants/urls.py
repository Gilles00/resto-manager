from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^getjson/commandes-pour/([0-9]*)', 'restaurants.views.get_commandes_as_json'),
    url(r'^getjson', 'restaurants.views.get_restaurants_as_json'),

	url(r'^self_manage', 'restaurants.views.self_manage_restaurants'),
    url(r'^add', 'restaurants.views.add_restaurant'),
    url(r'^edit/([0-9]*)', 'restaurants.views.edit_restaurant'),
    url(r'^delete/([0-9]*)', 'restaurants.views.delete_restaurant'),
    url(r'^undo_last_delete', 'restaurants.views.undo_last_delete'),
    url(r'^get/([0-9]*)', 'restaurants.views.get_restaurant'),
    url(r'', 'restaurants.views.show_restaurants'),
)
