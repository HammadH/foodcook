from django.views.generic import TemplateView


class LandingView(TemplateView):
	template_name = 'landing.html'

landing_view = LandingView.as_view()