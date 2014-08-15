from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, TemplateView, DetailView, View
from django.views.generic.edit import ModelFormMixin, FormView, UpdateView, FormMixin
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect

from utils import LoginRequiredMixin

from cooks.models import *
from cooks.forms import *



class NewCookProfileView(LoginRequiredMixin, CreateView):
	form_class = NewCookProfileForm
	template_name = 'cook_profile.html'

	def form_valid(self, form):
		self.object = form
		self.object.instance.user = self.request.user
		self.object.instance.save()    #TODO: remove this save()
		for area in form.cleaned_data.get('areas'):
			self.object.instance.areas.add(area)
		for cuisine in form.cleaned_data.get('cuisines'):
			self.object.instance.cuisines.add(cuisine)
		self.object.instance.save()
		return HttpResponseRedirect(reverse('cooks_detail_view', kwargs={'pk':self.object.instance.id}))

profile_view = NewCookProfileView.as_view()

class CookDetailsView(DetailView):
	model = Cook
	template_name = 'cook_detail.html'

	def get_context_data(self, **kwargs):
		kwargs['meals'] = self.object.meals.all()
		kwargs['form'] = EmailForm()
		return kwargs

	def post(self, request, *args, **kwargs):
		form = EmailForm(request.POST)
		if form.is_valid():
			cook = Cook.objects.get(id=request.POST.get('cook_id'))
			cook.send_email(form.cleaned_data)
			return HttpResponseRedirect(reverse('cooks_detail_view',  kwargs={'pk':self.kwargs['pk']}))
		else:
			pass
			
			
	
	


detail_view = CookDetailsView.as_view()

class DisplayCooks(FormMixin, ListView):
	model = Cook
	template_name = 'cooks_list.html'

	def get_context_data(self, **kwargs):
		context = super(DisplayCooks, self).get_context_data(**kwargs)
		context['form'] = CookSearchForm()
		return context

	def get_queryset(self):
		search_area = CookSearchForm(self.request.GET)
		if search_area and search_area.is_valid():
			area = search_area.cleaned_data.get('area')
			return Cook.objects.filter(areas__name__icontains=area)
		else:
			return Cook.objects.all()

		

	def form_valid(self, form):
		import pdb;pdb.set_trace()

	



list_view = DisplayCooks.as_view()	 



class CongratsView(LoginRequiredMixin, TemplateView):
	template_name = 'congrats.html'

congrats_view = CongratsView.as_view()

class EditProfileView(LoginRequiredMixin, UpdateView):
	model = Cook
	form_class = NewCookProfileForm
	fields = ['image', 'mobile', 'cuisines', 'breakfast', 
			'lunch', 'dinner', 'price', 'areas', 'info', 'area_info']
	template_name = 'cook_profile_update.html'


	def get_object(self, queryset=None):
		profile = Cook.objects.get(user=self.request.user)
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