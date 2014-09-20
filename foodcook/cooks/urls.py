from django.conf.urls import patterns, include, url


from cooks import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'foodcook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	# url(r'^new/$', views.cookinginfo, name='cookinginfo_form'),
	# url(r'^new/neighbourhood/$', views.neighbourhood_view, name='select_neighbourhood'),
	url(r'^$', views.list_view, name='cooks_list_view'),
	url(r'^profile/(?P<pk>\d+)/$', views.detail_view, name='cooks_detail_view'),
	url(r'^profile/new/cooking/$', views.new_cook_cooking_details, name='new_profile_view'),
	# url(r'^profile/new/price/$', views.cooking_details, name='new_profile_view'),
	# url(r'^profile/new/place/$', views.cooking_details, name='new_profile_view'),
	url(r'^profile/edit/$', views.edit_profile_view, name='edit_profile_view'),
	# url(r'^profile/delete/$', views.profile_view, name='my_profile_view'),
	url(r'^meal/new/$', views.new_meal, name='new_meal'),
	url(r'^meal/edit/(?P<pk>\d+)$', views.edit_meal, name='edit_meal'),
	url(r'^meal/delete/(?P<pk>\d+)$', views.delete_meal, name='delete_meal'),
	# url(r'^sort/$', views.sort_list, name='sort_list'),
	url(r'^mobile_click/', views.mobile_click_counter, name='count_mobile_click_lead'),

	# url(r'^new/congrats/$', views.congrats_view, name='congrats_view'),

	
)

