from django.db import models
from django.contrib.auth import get_user_model
from django.contrib import admin

from sorl.thumbnail import ImageField


User = get_user_model()


def get_profile_image_path(instance, filename):
	return "cooks/%s/profile_pics/%s" %(instance, filename)

class Area(models.Model):
	name = models.CharField(max_length=100, blank=False)

	def __unicode__(self):
		return self.name

class Cook(models.Model):
	user = models.ForeignKey(User, unique=True, blank=False)
	image = ImageField(upload_to=get_profile_image_path, blank=True) #TODO: add default image
	mobile = models.CharField(max_length=10, blank=True)
	cuisines = models.TextField(blank=False)
	breakfast = models.BooleanField(blank=False)
	lunch = models.BooleanField(blank=False)
	dinner = models.BooleanField(blank=False)
	price = models.IntegerField(blank=False)
	neighbourhood = models.ManyToManyField(Area)


	def __unicode__(self):
		return self.user.username

	def get_absolute_url(self):
		from django.core.urlresolvers import reverse
		return reverse('cooks_detail_view', kwargs={'pk':str(self.id)})

	@staticmethod
	def get_search_queryset(params):
		"""
		filters and returns cooks based on search params
		params is  searchform.cleaned_data
		"""
		area = params.get('area')
		qset = Q(pk__gt=0)
		if area:
			qset &= Q(neighbourhood__icontains=area)
		return qset
	
	
	
admin.site.register(Area)




# admin.site.register(Profile)

# admin.site.register(CookingInfo)

# admin.site.register(Neighbourhood)

