from django.views.generic import View, TemplateView, DetailView
from django.views.generic.edit import FormMixin, FormView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

from cooks.forms import *
from cooks.models import EventFood, EverydayFood, BakedFood, Cook

from utils import LoginRequiredMixin

class LandingView(FormMixin, ListView):
	template_name = 'landing.html'
	model = Cook
	queryset = Cook.objects.filter(is_featured=False)
	
	def get_context_data(self, **kwargs):
		context = super(LandingView, self).get_context_data(**kwargs)
		context['featured_cooks'] = Cook.objects.filter(is_featured=True)[:3]
		context['eventfood'] = EventFood.objects.all()
		context['everydayfood'] = EverydayFood.objects.all()
		context['form'] = CookSearchForm()
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

food_success = FoodPostSuccess.as_view()

class EverydayfoodDetailsView(LoginRequiredMixin, FormMixin, DetailView):
	model = EverydayFood
	form_class = EmailForm
	pk_url_kwarg = 'pk'
	template_name = 'food_details.html'

everydayfood_details = EverydayfoodDetailsView.as_view()

