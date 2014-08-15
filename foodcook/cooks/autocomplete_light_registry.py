import autocomplete_light

from models import Area, Cuisines

autocomplete_light.register(Area, search_fields=('name',),
	autocomplete_js_attributes={'placeholder':'Dubai Marina..'})

autocomplete_light.register(Cuisines, search_fields=('name',),
	autocomplete_js_attributes={'placeholder':'Dubai Marina..'})


