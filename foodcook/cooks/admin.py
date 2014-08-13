from django.contrib import admin

import autocomplete_light

from models import Cook

class CookAdmin(admin.ModelAdmin):
	form = autocomplete_light.modelform_factory(Cook)

admin.site.register(Cook, CookAdmin)
