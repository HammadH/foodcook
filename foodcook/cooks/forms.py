from django import forms

import autocomplete_light

from cooks.models import Cook, Area

# class NewCookProfileForm(forms.ModelForm):
# 	class Meta:
# 		model = Cook
# 		widgets = autocomplete_light.get_widgets_dict(Cook)
# 		exclude=['user']

# NewCookProfileForm = autocomplete_light.modelform_factory(Cook, autocomplete_exclude=['user',], registry=Area)

class NewCookProfileForm(autocomplete_light.ModelForm):
	class Meta:
		model = Cook
		exclude = ['user',]
		
class CookSearchForm(forms.Form):
	area = forms.CharField()

	