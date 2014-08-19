from django import forms

import autocomplete_light
from autocomplete_light.widgets import TextWidget, MultipleChoiceWidget, ChoiceWidget

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
		'image': ImageWidget(attrs={'onchange':'upload_img(this)'}),
		'cuisines':MultipleChoiceWidget('CuisinesAutocomplete', attrs={'class':'form-control', 'placeholder':'eg. Chinese, Italian'}),
		'full_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your name '}),
		'mobile': forms.TextInput(attrs={'class':'form-control', 'placeholder':'eg. 0552051301'}),
		'intro': forms.Textarea(attrs={'class':'form-control', 'placeholder':'I cook different meals everyday. My food is very healthy and you can contact me anytime..', 'rows':3}),
		# 'breakfast': forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-control'})),
		# 'lunch': forms.TextInput(attrs={'class':'form-control', 'placeholder':'eg. 0552051301'}),
		# 'dinner': forms.TextInput(attrs={'class':'form-control', 'placeholder':'eg. 0552051301'}),
		'price': forms.TextInput(attrs={'class':'form-control', 'placeholder':'eg. 20'}),
		'areas': MultipleChoiceWidget('AreaAutocomplete', attrs={'class':'form-control', 'placeholder':'eg. Dubai Marina, JLT'}),
		'area_info': forms.TextInput(attrs={'class':'form-control', 'placeholder':'eg. Marina Pinnacle, near Marina Walk'}),
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
	area = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter area to search..'}))


class EmailForm(forms.Form):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Enter your email'}))
	message = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
