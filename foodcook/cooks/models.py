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
	created_at = models.DateTimeField(auto_now_add=True, null=True)

	def __unicode__(self):
		return self.name.split('-')[0]

class Cuisine(models.Model):
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
	image = ImageField("Profile picture", upload_to=get_profile_image_path, blank=True, max_length=1000,default=settings.DEFAULT_PROFILE_IMAGE_PATH)
	mobile = models.CharField(max_length=10, blank=True)
	intro = models.TextField(blank=True)
	place_slug = models.CharField(max_length=150, null=True, blank=False)
	area = models.ForeignKey(Area, null=True, blank=True)
	cuisines = models.ManyToManyField(Cuisine, blank=False, null=True)
	breakfast = models.BooleanField(blank=False, default=False)
	lunch = models.BooleanField(blank=False, default=False)
	dinner = models.BooleanField(blank=False, default=False)
	min_price = models.IntegerField(blank=False, null=True)
	max_price = models.IntegerField(blank=False, null=True)
	area_info = models.TextField(blank=True)
	cook_type = models.ForeignKey(CookType, blank=False, null=True, default='Unspecified')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(blank=True, null=True) # when the cook updates profile.
	is_featured = models.BooleanField(blank=True, default=False)
	


	def __unicode__(self):
		return self.user.email

	def get_absolute_url(self):
		from django.core.urlresolvers import reverse
		return reverse('cooks_detail_view', kwargs={'pk':str(self.id)})

	def get_price_range(self):
		return "%s-%s AED" %(self.min_price, self.max_price)

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
	created_at = models.DateTimeField(auto_now_add=True, null=True)

	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('edit_meal', kwargs={'pk':str(self.id)})

class Event(models.Model):
	'''Represents types of events'''
	name = models.CharField(max_length=100, blank=False)
	created_at = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.name


class FoodBase(models.Model):
	message = models.TextField('Message',)
	place_slug = models.CharField('Area', max_length=150, null=True, blank=False)
	area = models.ForeignKey(Area, null=True, blank=True)
	email = models.EmailField('Email',)
	phone = models.CharField('Mobile',max_length=10, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	

	class Meta:
		abstract = True

	def save(self):
		if self.place_slug:
			area, created = Area.objects.get_or_create(name=self.place_slug)
			self.area = area
			super(FoodBase, self).save()

	def get_absolute_url(self):
		return reverse('food', kwargs={'pk':self.id})

class EverydayFood(FoodBase):
	cuisines = models.ManyToManyField(Cuisine, blank=True, null=True)
	breakfast = models.BooleanField(blank=False, default=False)
	lunch = models.BooleanField(blank=False, default=False)
	dinner = models.BooleanField(blank=False, default=False)

class EventFood(FoodBase):
	cuisines = models.ManyToManyField(Cuisine, blank=True, null=True)
	time = models.DateTimeField('Time of event', blank=True, null=True)
	people = models.IntegerField('How many people', blank=True, null=True)
	event = models.ForeignKey(Event, blank=False, null=True)

class BakedFood(FoodBase):
	time = models.DateTimeField('When do you need it?',blank=True, null=True)
	item = models.CharField('What do you want?', max_length=100, blank=True, null=True)




class MobileClickLead(models.Model):
	cook = models.ForeignKey(Cook)
	created_at = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return 'mobile click lead for %s' %self.cook

class EmailLead(models.Model):
	'''For cooks; when users contact them'''
	cook = models.ForeignKey(Cook)
	email = models.EmailField()
	message = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True, null=True)

	def __unicode__(self):
		return 'Email lead for %s from %s' %(self.cook, self.email)

class UserSubscription(models.Model):
	email = models.EmailField()
	areas = models.ManyToManyField(Area, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, null=True)

	def __unicode__(self):
		return self.email


admin.site.register(Area)
admin.site.register(Cuisine)
admin.site.register(Meal)
admin.site.register(CookType)
admin.site.register(MobileClickLead)
admin.site.register(EmailLead)
admin.site.register(UserSubscription)
admin.site.register(EventFood)
admin.site.register(EverydayFood)
admin.site.register(BakedFood)
admin.site.register(Event)


# admin.site.register(Profile)

# admin.site.register(CookingInfo)



