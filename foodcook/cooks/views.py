import json

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, TemplateView, DetailView, View
from django.views.generic.edit import ModelFormMixin, FormView, UpdateView, FormMixin, BaseCreateView
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect, HttpResponse

from utils import LoginRequiredMixin

from cooks.models import *
from cooks.forms import *



class CookSignUpView_CookingDetails(LoginRequiredMixin,  CreateView):
	form_class = NewCookProfileForm
	template_name = 'new_cook_form.html'

	def form_valid(self, form):
		data = form.cleaned_data
		self.object = form
		self.object.instance.user = self.request.user

		  #TODO: remove this save()
		self.object.instance.area,created_new = Area.objects.get_or_create(name=data.get('place_slug'))
		self.object.instance.save()
		for cuisine in data.get('cuisines'):
			self.object.instance.cuisines.add(cuisine)
		self.object.instance.save()
		return HttpResponseRedirect(reverse('cooks_detail_view', kwargs={'pk':self.object.instance.id}))

new_cook_cooking_details = CookSignUpView_CookingDetails.as_view()



class CookDetailsView(DetailView):
	model = Cook
	template_name = 'cook_detail.html'
	context_object_name = 'cook'

	def get_context_data(self, **kwargs):
		kwargs['meals'] = self.object.meals.all()
		kwargs['form'] = EmailLeadForm()
		return kwargs

	def post(self, request, *args, **kwargs):
		form = EmailLeadForm(request.POST)
		if form.is_valid():
			cook = Cook.objects.get(id=request.POST.get('cook_id'))
			data = form.cleaned_data
			cook.send_email(data)
			email_lead = EmailLead(cook=cook, email=data['email'], message=data['message'])
			email_lead.save()			
			return HttpResponseRedirect(reverse('cooks_list_view'))
		else:
			pass
			 
detail_view = CookDetailsView.as_view()

class DisplayCooks(FormMixin, ListView):
	model = Cook
	template_name = 'cooks_list.html'

	def get_context_data(self, **kwargs):
		context = super(DisplayCooks, self).get_context_data(**kwargs)
		context['form'] = CookSearchForm()
		context['subscription_form'] = UserSubscriptionForm()
		return context

	def get_queryset(self):
		search_area = CookSearchForm(self.request.GET)
		if search_area and search_area.is_valid():
			area = search_area.cleaned_data.get('area')
			return Cook.objects.filter(area__name__icontains=area)
		else:
			return Cook.objects.all()


	def post(self, request, *args, **kwargs):
		form = UserSubscriptionForm(request.POST)
		if form.is_valid():
			try:
				area, created = Area.objects.get_or_create(name=self.request.GET.get('area'))
			except:
				return HttpResponseRedirect('/')
			new_subscription = UserSubscription(area=area, email=form.cleaned_data['email'])
			new_subscription.save()
			return HttpResponseRedirect('/')
		else:
			return HttpResponseRedirect('/')


list_view = DisplayCooks.as_view()	 



class CongratsView(LoginRequiredMixin, TemplateView):
	template_name = 'congrats.html'

congrats_view = CongratsView.as_view()

class EditProfileView(LoginRequiredMixin, UpdateView):
	
	model = Cook
	form_class = NewCookProfileForm
	template_name = 'cook_profile_update.html'

	def get_object(self, queryset=None):
		try:
			profile = Cook.objects.get(user=self.request.user)
		except Cook.DoesNotExist:

			profile = Cook(user=self.request.user)   # redirect to a new profile..
		return profile

	def get_success_url(self):
		return reverse('cooks_detail_view', kwargs={'pk':self.object.id})

edit_profile_view = EditProfileView.as_view()



class NewMealView(LoginRequiredMixin, FormView):
	form_class = MealForm
	template_name = 'new_meal.html'

	def get_initial(self):
		self.initial['cook'] = self.request.user.cook_set.get()
		return self.initial
		
	def form_valid(self, form):
		form.instance.cook = form.initial['cook']
		form.save()
		return HttpResponseRedirect(self.get_success_url())

	def get_success_url(self):
		return reverse('cooks_detail_view', kwargs={'pk':self.request.user.cook_set.get().id})

new_meal = NewMealView.as_view()


class EditMealView(LoginRequiredMixin, UpdateView):
	model = Meal
	form_class = MealForm
	fields = ['name','image']
	template_name = 'edit_meal.html'
	

	def get_object(self, queryset=None):
		return Meal.objects.get(id=self.kwargs['pk'])

	def get_success_url(self):
		return reverse('cooks_detail_view', kwargs={'pk':self.request.user.cook_set.get().id})
		

edit_meal = EditMealView.as_view()

class DeleteMealView(LoginRequiredMixin, View):
	def get(self, request, *args, **kwargs):
		meal = Meal.objects.get(id=self.kwargs['pk'])
		meal.delete()
		return HttpResponseRedirect(reverse('cooks_detail_view', kwargs={'pk':self.request.user.cook_set.get().id}))

delete_meal = DeleteMealView.as_view()

def mobile_click_counter(request):
	if request.is_ajax():
		try:
			MobileClickLead.objects.create(cook=Cook.objects.get(id=int(request.GET.get('id'))))
			return HttpResponse(json.dumps({'status':'success'}), content_type='application/json')
		except:
			return HttpResponse(json.dumps({'status':'failed'}), content_type='application/json')
	

		
