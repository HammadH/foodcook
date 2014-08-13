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
		self.object.instance.save()
		return HttpResponseRedirect(reverse('cooks_detail_view', kwargs={'pk':self.request.user.id}))

profile_view = NewCookProfileView.as_view()

class CookDetailsView(DetailView):
	model = Cook
	pk_url_kwarg = 'pk'
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
			return Cook.objects.filter(neighbourhood__icontains=area)
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
	fields = ['nationality', 'mobile']
	template_name = 'cook_profile_update.html'


	def get_object(self, queryset=None):
		profile = Cook.objects.get(id=self.request.user.id)
		return profile

	def get_success_url(self):
		import pdb;pdb.set_trace()
		return reverse('cooks_detail_view', kwargs={'pk':self.request.user.id})

edit_profile_view = EditProfileView.as_view()