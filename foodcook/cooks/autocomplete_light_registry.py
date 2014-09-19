import autocomplete_light

from models import Cuisine



autocomplete_light.register(Cuisine, search_fields=('name',),
	autocomplete_js_attributes={'placeholder':'Dubai Marina..'})

