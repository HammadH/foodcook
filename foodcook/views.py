from django.views.generic import View, TemplateView, DetailView
from django.views.generic.edit import FormMixin, FormView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from django.contrib.auth import logout
from django.shortcuts import render_to_response

from allauth.account.forms import SignupForm
from cooks.forms import *
from cooks.models import EventFood, EverydayFood, BakedFood, Cook

from utils import LoginRequiredMixin

mail_subject = 'You have a cook!'
from_email = 'findcooks@44cooks.com'

class LandingView(FormView):
	template_name = 'landing.html'
	form_class = SignupForm
	redirect_field_name = "next"
	success_url = None

	def get_context_data(self, **kwargs):
		context = super(LandingView, self).get_context_data(**kwargs)
		context['featured_everyday_cooks'] = Cook.objects.filter(is_featured=True, cook_type__name__icontains='Everyday Cook')[:3]
		context['featured_special_cooks'] = Cook.objects.filter(is_featured=True, cook_type__name__icontains='Special Cook')[:3]
		context['eventfood'] = EventFood.objects.order_by('-created_at')[:5]
		context['everydayfood'] = EverydayFood.objects.order_by('-created_at')[:5]
		context['bakedfood'] = BakedFood.objects.order_by('-created_at')[:5]
		context['form'] = SignupForm()
		return context

	def form_valid(self, form):
		return reverse('cooks_list_view')



landing_view = LandingView.as_view()


class LoginCheck(View):
	"""
	checks if the user is cook and redirects to appropriate profile
	"""
	def get(self, request, *args, **kwargs):
		try:
			cook = request.user.cook_set.get()
			return HttpResponseRedirect(reverse('cooks_detail_view', kwargs={'pk':str(cook.id)}))
		except Cook.DoesNotExist, AttributeError:
			return HttpResponseRedirect(reverse('new_profile_view'))

check_and_login = LoginCheck.as_view()


class ContactView(FormView):
	form_class = EmailForm
	template_name = 'contact.html'

	def form_valid(self, form):

		data = form.cleaned_data

		subject = 'From 44Cooks'
		message =  "Message from %s  %s" %(data.get('email'), data.get('message'))
		from_email = 'findcooks@44Cooks.com'


		send_mail(subject, message, from_email, ['hammadsyed9@gmail.com'])

		return HttpResponseRedirect('/')

contact_view = ContactView.as_view()

class BlogView(TemplateView):
	template_name = 'intro_blog.html'

intro_blog = BlogView.as_view()


class EverydayFoodFormView(FormView):
	form_class = EverydayFoodForm
	template_name = 'everydayfood_form.html'
	success_url = '/success'

	def form_valid(self, form):
		form.save()
		return HttpResponseRedirect(self.get_success_url())

new_everyday_food = EverydayFoodFormView.as_view()

class EventFoodFormView(FormView):
	form_class = EventFoodForm
	template_name = 'eventfood_form.html'
	success_url = '/success'

	def form_valid(self, form):
		form.save()
		return HttpResponseRedirect(self.get_success_url())

new_event_food = EventFoodFormView.as_view()

class BakedFoodFormView(FormView):
	form_class = BakedFoodForm
	template_name = 'bakedfood_form.html'
	success_url = '/success'

	def form_valid(self, form):
		form.save()
		return HttpResponseRedirect(self.get_success_url())

new_baked_food = BakedFoodFormView.as_view()

class FoodPostSuccess(TemplateView):
	template_name = 'food_success.html'

	def get(self, request, *args, **kwargs):
		logout(request)
		return render_to_response('food_success.html')

food_success = FoodPostSuccess.as_view()


class EverydayfoodDetailsView(LoginRequiredMixin, DetailView):
	model = EverydayFood
	template_name = 'everydayfood_details.html'
	pk_url_kwarg = 'pk'
	context_object_name = 'food'

	def get_context_data(self, **kwargs):
		context = super(EverydayfoodDetailsView, self).get_context_data(**kwargs)
		context['form'] = EmailForm()
		return context

	def post(self, request, *args, **kwargs):
		message = request.POST.get('message')
		send_mail(mail_subject, message, from_email, [self.get_object().email])
		return HttpResponse('Your message was sent')


everydayfood_details = EverydayfoodDetailsView.as_view()

class EventfoodDetailsView(LoginRequiredMixin, DetailView):
	model = EventFood
	template_name = 'eventfood_details.html'
	pk_url_kwarg = 'pk'
	context_object_name = 'food'

	def get_context_data(self, **kwargs):
		context = super(EventfoodDetailsView, self).get_context_data(**kwargs)
		context['form'] = EmailForm()
		return context

	def post(self, request, *args, **kwargs):
		message = request.POST.get('message')
		send_mail(mail_subject, message, from_email, [self.get_object().email])
		return HttpResponse('Your message was sent')

eventfood_details = EventfoodDetailsView.as_view()

class BakedfoodDetailsView(LoginRequiredMixin, DetailView):
	model = BakedFood
	template_name = 'bakedfood_details.html'
	pk_url_kwarg = 'pk'
	context_object_name = 'food'

	def get_context_data(self, **kwargs):
		context = super(BakedfoodDetailsView, self).get_context_data(**kwargs)
		context['form'] = EmailForm()
		return context

	def post(self, request, *args, **kwargs):
		message = request.POST.get('message')
		send_mail(mail_subject, message, from_email, [self.get_object().email])
		return HttpResponse('Your message was sent')

bakedfood_details = BakedfoodDetailsView.as_view()

class FoodSelectView(TemplateView):
	template_name = 'food_select.html'

choose_food = FoodSelectView.as_view()

