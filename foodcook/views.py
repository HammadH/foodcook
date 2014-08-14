from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse

from cooks.forms import CookSearchForm

class LandingView(FormView):
	template_name = 'landing.html'
	form_class = CookSearchForm

	def form_valid(self, form):
		return reverse('cooks_list_view')

landing_view = LandingView.as_view()