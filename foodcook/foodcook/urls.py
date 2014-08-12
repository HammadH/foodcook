from django.conf.urls import patterns, include, url

import autocomplete_light
autocomplete_light.autodiscover()

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'foodcook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', 'views.landing_view', name='landing_view'),
	url(r'^admin/', include(admin.site.urls)),

	url(r'^accounts/', include('allauth.urls')),
	url(r'^cooks/', include('cooks.urls')),
	
)
