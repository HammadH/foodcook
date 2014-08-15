from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, TemplateView, DetailView
from django.views.generic.edit import ModelFormMixin, FormView, UpdateView, FormMixin
from django.views.generic.list import ListView

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