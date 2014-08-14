from django.conf.urls import patterns, include, url


from cooks import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'foodcook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	# url(r'^new/$', views.cookinginfo, name='cookinginfo_form'),
	# url(r'^new/neighbourhood/$', views.neighbourhood_view, name='select_neighbourhood'),
	url(r'^$', views.list_view, name='cooks_list_view'),
	url(r'^profile/(?P<pk>[0-9])/$', views.detail_view, name='cooks_detail_view'),
	url(r'^profile/new/$', views.profile_view, name='new_profile_view'),
	url(r'^profile/edit/$', views.edit_profile_view, name='edit_profile_view'),
	url(r'^profile/delete/$', views.profile_view, name='my_profile_view'),

	# url(r'^new/congrats/$', views.congrats_view, name='congrats_view'),

	
)

