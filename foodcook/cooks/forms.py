from django import forms

import autocomplete_light
from autocomplete_light.widgets import TextWidget, MultipleChoiceWidget, ChoiceWidget

from cooks.models import *

from form_utils.widgets import ImageWidget

DISABLE_FORM_SUBMIT_ON_PLACE_SELECT = "if($('.pac-container').is(':visible') && event.keyCode == 13) {event.preventDefault();}"
# from form_utils.forms import BetterModelForm, BetterModelFormMetaclass

# class NewCookProfileForm(forms.ModelForm):
# 	class Meta:
# 		model = Cook
# 		widgets = autocomplete_light.get_widgets_dict(Cook)
# 		exclude=['user']

# NewCookProfileForm = autocomplete_light.modelform_factory(Cook, autocomplete_exclude=['user',], registry=Area)

EverydayFoodPlaceholder ="Hi, \nI am looking for someone who can provide me dinner everyday.\nFeel free to contact me anytime."
EventFoodPlaceholder = "Hi, \nI am looking for someone to cook food for a party on..."
BakedFoodPlaceholder = "Hi, \nI am looking for someone to bake a Cheese cake on..."

class SignupForm(forms.Form):
	first_name = forms.CharField(max_length=50, label="First Name")
	last_name = forms.CharField(max_length=50, label="Last Name")

	def signup(self, request, user):
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.save()

class NewCookProfileForm(autocomplete_light.ModelForm):
	class Meta:
		model = Cook
		#fields = ('image', 'full_name', 'intro')
		exclude = ['user', 'created_at', 'updated_at', 'min_price', 'max_price', 'cook_type']
		widgets = {
		'image': forms.FileInput(attrs={'onchange':'upload_img(this)'}),
		'cuisines':MultipleChoiceWidget('CuisineAutocomplete', attrs={'class':'form-control', 'placeholder':'eg. Chinese, Italian'}),
		'mobile': forms.TextInput(attrs={'class':'form-control', 'placeholder':'eg. 0552051301', }),
		'intro': forms.Textarea(attrs={'class':'form-control', 'placeholder':'I cook different meals everyday. My food is very healthy and you can contact me anytime..', 'rows':3}),
		# 'breakfast': forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-control'})),
		# 'lunch': forms.TextInput(attrs={'class':'form-control', 'placeholder':'eg. 0552051301'}),
		# 'dinner': forms.TextInput(attrs={'class':'form-control', 'placeholder':'eg. 0552051301'}),
		# 'cook_type': forms.RadioSelect(attrs={'class':'form-control ', 'style':'margin-left:10px;'}, ),
		# 'min_price': forms.NumberInput(attrs={'class':'form-control', 'style':'width:70px;', 'id':'min_price'}),
		# 'max_price': forms.NumberInput(attrs={'class':'form-control', 'style':'width:70px;'}),
		'place_slug': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Type your location and select..', 'id':'place-input','onkeydown':DISABLE_FORM_SUBMIT_ON_PLACE_SELECT}),
		'area_info': forms.TextInput(attrs={'class':'form-control', 'placeholder':'eg. Marina Pinnacle, near Marina Walk'}),
		}
		
class EverydayFoodForm(autocomplete_light.ModelForm):
	class Meta:
		model = EverydayFood
		exclude = ['area']
		widgets = {
			'message': forms.Textarea(attrs={'class':'form-control', 'rows':3, 'style':'margin-bottom:10px;', 'placeholder':EverydayFoodPlaceholder}),
			'place_slug': forms.TextInput(attrs={'class':'form-control','id':'location_input', 'placeholder':'Enter your location','style':'margin-bottom:10px;','onkeydown':DISABLE_FORM_SUBMIT_ON_PLACE_SELECT}),
			'email': forms.EmailInput(attrs={'class':'form-control','style':'margin-bottom:10px;','placeholder':'Your email'}),
			'phone': forms.TextInput(attrs={'class':'form-control','placeholder':'Your mobile'}),
			'cuisines':MultipleChoiceWidget('CuisineAutocomplete', attrs={'class':'form-control', 'placeholder':'eg. Chinese, Italian', }),
		}

class EventFoodForm(autocomplete_light.ModelForm):
	class Meta:
		model = EventFood
		exclude = ['area']
		widgets = {
			'message': forms.Textarea(attrs={'class':'form-control', 'rows':3, 'style':'margin-bottom:10px;', 'placeholder':EventFoodPlaceholder}),
			'cuisines':MultipleChoiceWidget('CuisineAutocomplete', attrs={'class':'form-control', 'placeholder':'eg. Chinese, Italian'}),
			'place_slug': forms.TextInput(attrs={'class':'form-control','id':'location_input', 'placeholder':'Enter your location','style':'margin-bottom:10px;', 'onkeydown':DISABLE_FORM_SUBMIT_ON_PLACE_SELECT}),
			'email': forms.EmailInput(attrs={'class':'form-control','style':'margin-bottom:10px;','placeholder':'Your email'}),
			'phone': forms.TextInput(attrs={'class':'form-control','placeholder':'Your mobile'}),
			'time':forms.DateTimeInput(attrs={'placeholder':'eg: 2006-10-25 14:30:59'})
			
		}

class BakedFoodForm(forms.ModelForm):
	class Meta:
		model = BakedFood
		exclude = ['area']
		widgets = {
			'message': forms.Textarea(attrs={'class':'form-control', 'rows':3, 'style':'margin-bottom:10px;', 'placeholder':BakedFoodPlaceholder}),
			'place_slug': forms.TextInput(attrs={'class':'form-control','id':'location_input', 'placeholder':'Enter your location','style':'margin-bottom:10px;', 'onkeydown':DISABLE_FORM_SUBMIT_ON_PLACE_SELECT}),
			'item': forms.TextInput(attrs={'class':'form-control', 'placeholder':'eg: Cheese cake, choco chip cookies'}),
			'time':forms.DateTimeInput(attrs={'placeholder':'eg: 2006-10-25 14:30:59'})
		}


class MealForm(forms.ModelForm):
	class Meta:
		model = Meal
		exclude = ['cook',]
		widgets = {
		'image': ImageWidget(),
		}


class CookSearchForm(forms.Form):
	area = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your location..','id':'location_input'},))
	


class EmailLeadForm(forms.ModelForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Enter your email'}))
	message = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
	

	class Meta:
		model = EmailLead
		exclude = ['cook']


class EmailForm(forms.Form):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Enter your email'}))
	message = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))


class UserSubscriptionForm(forms.ModelForm):
	class Meta:
		model = UserSubscription
		exclude = ['area']
		widgets = {
		'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'YOUR EMAIL ADDRESS', 'style':'height:40px;'})
		}


