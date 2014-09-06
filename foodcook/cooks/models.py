import os

from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.core.mail import send_mail

from django.conf import settings

from sorl.thumbnail import ImageField



	

def get_profile_image_path(instance, filename):
	return os.path.join(settings.MEDIA_ROOT, 'cooks_data/%s/profile_pics/%s' %(instance, filename)) 

def get_meal_image_path(instance, filename):
	return os.path.join(settings.MEDIA_ROOT, 'cooks_data/%s/meals/%s' %(instance.cook, filename))


class Area(models.Model):
	name = models.CharField(max_length=100, blank=False)

	def __unicode__(self):
		return self.name

class Cuisines(models.Model):
	name = models.CharField(max_length=100, blank=False)

	def __unicode__(self):
		return self.name

class CookType(models.Model):
	name = models.CharField(max_length=100, blank=False)

	def __unicode__(self):
		return self.name


# class Rating(models.Model):


class Cook(models.Model):
	user = models.ForeignKey(User, unique=True, blank=False)
	image = ImageField("Profile picture", upload_to=get_profile_image_path, blank=True, default=settings.DEFAULT_PROFILE_IMAGE_PATH)
	mobile = models.CharField(max_length=10, blank=True)
	intro = models.TextField(blank=True)
	areas = models.ManyToManyField(Area)
	cuisines = models.ManyToManyField(Cuisines, blank=False)
	breakfast = models.BooleanField(blank=False)
	lunch = models.BooleanField(blank=False)
	dinner = models.BooleanField(blank=False)
	min_price = models.IntegerField(blank=False, null=True)
	max_price = models.IntegerField(blank=False, null=True)
	area_info = models.TextField(blank=True)
	cook_type = models.ForeignKey(CookType, blank=False, null=True, default='Unspecified')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(blank=True, null=True) # when the cook updates profile.
	


	def __unicode__(self):
		return self.user.email

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
			qset &= Q(areas__name__icontains=area)
		return qset

	def send_email(self, data):
		'''
		used to send email to self
		data: form.cleaned_data
		'''
		subject = "Someone is interested in your cooking"
		message =  "Message from %s  %s" %(data.get('email'), data.get('message'))
		from_email = 'findcooks@44Cooks.com'
		recipient_list = [self.user.email]
		send_mail(subject, message, from_email, recipient_list)
		return True


class Meal(models.Model):
	name = models.CharField(max_length=50, blank=False)
	image = ImageField(upload_to= get_meal_image_path, blank=False)
	cook = models.ForeignKey(Cook, related_name = 'meals')

	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('edit_meal', kwargs={'pk':str(self.id)})

admin.site.register(Area)
admin.site.register(Cuisines)
admin.site.register(Meal)
admin.site.register(CookType)


# admin.site.register(Profile)

# admin.site.register(CookingInfo)



