from django.views.generic import View
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from cooks.forms import CookSearchForm
from cooks.models import Cook

class LandingView(FormView):
	template_name = 'landing.html'
	form_class = CookSearchForm

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