from django.contrib import admin
from django.conf.urls import patterns, include, url
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'RestoManager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^notify', 'notifications.views.notify'),

	url(r'^sendemail', 'notifications.views.send_email'),
)
