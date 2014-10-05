from django.views.generic import View, TemplateView
from django.views.generic.edit import FormMixin, FormView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

from cooks.forms import CookSearchForm, EmailForm
from cooks.models import Cook, UserSubscription

class LandingView(FormMixin, ListView):
	template_name = 'landing.html'
	model = Cook
	
	def get_context_data(self, **kwargs):
		context = super(LandingView, self).get_context_data(**kwargs)
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