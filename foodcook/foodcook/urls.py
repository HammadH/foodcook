from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static




import autocomplete_light
autocomplete_light.autodiscover()

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'foodcook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', 'views.landing_view', name='landing_view'),
	url(r'^contact/$', 'views.contact_view', name='contact_view'),
	url(r'^login/', 'views.check_and_login', name='check_and_login'),

	url(r'^admin/', include(admin.site.urls)),
	url(r'^autocomplete/', include('autocomplete_light.urls')),
	url(r'^accounts/', include('allauth.urls')),
	url(r'^cooks/', include('cooks.urls')),
	url(r'^what-is-44cooks/$', 'views.intro_blog', name='intro_blog'),
	
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
    )