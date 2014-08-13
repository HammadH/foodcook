import autocomplete_light

from models import Area

autocomplete_light.register(Area, search_fields=('name',),
	autocomplete_js_attributes={'placeholder':'enter area name..'})

