from django import forms

import autocomplete_light

from cooks.models import Cook, Area, Meal

from form_utils.widgets import ImageWidget
# from form_utils.forms import BetterModelForm, BetterModelFormMetaclass

# class NewCookProfileForm(forms.ModelForm):
# 	class Meta:
# 		model = Cook
# 		widgets = autocomplete_light.get_widgets_dict(Cook)
# 		exclude=['user']

# NewCookProfileForm = autocomplete_light.modelform_factory(Cook, autocomplete_exclude=['user',], registry=Area)

class NewCookProfileForm(autocomplete_light.ModelForm):
	class Meta:
		model = Cook
		#fields = ('image', 'full_name', 'intro')
		exclude = ['user',]
		widgets = {
		'image': ImageWidget(),
		}
		
# class BaseNewCookProfileForm(BetterModelForm):
	
# 	class Meta:
# 		model = Cook
# 		exclude = ['user',]
# 		fieldsets = [('Profile', {'fields':['image', 'full_name', 'intro'], }),
# 		('Cooking', {'fields':['cuisines', 'breakfast', 'lunch', 'dinner', 'price'], 'description':'Advanced_stuff', 'placeholder':'intr'}),
# 		('Neighbourhood', {'fields':['area','area_info']}),
# 		('Contact', {'fields':['mobile']})]



class MealForm(forms.ModelForm):
	class Meta:
		model = Meal
		exclude = ['cook',]
		widgets = {
		'image': ImageWidget(),
		}


class CookSearchForm(forms.Form):
	area = forms.CharField()

class EmailForm(forms.Form):
	email = forms.EmailField()
	message = forms.CharField()