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
		exclude = ['user', 'created_at', 'updated_at']
		widgets = {
		'image': ImageWidget(attrs={'onchange':'upload_img(this)'}),
		'cuisines':MultipleChoiceWidget('CuisinesAutocomplete', attrs={'class':'form-control', 'placeholder':'eg. Chinese, Italian'}),
		'mobile': forms.TextInput(attrs={'class':'form-control', 'placeholder':'eg. 0552051301'}),
		'intro': forms.Textarea(attrs={'class':'form-control', 'placeholder':'I cook different meals everyday. My food is very healthy and you can contact me anytime..', 'rows':3}),
		# 'breakfast': forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-control'})),
		# 'lunch': forms.TextInput(attrs={'class':'form-control', 'placeholder':'eg. 0552051301'}),
		# 'dinner': forms.TextInput(attrs={'class':'form-control', 'placeholder':'eg. 0552051301'}),
		'price_regular': forms.TextInput(attrs={'class':'form-control', 'placeholder':'eg. 20'}),
		'price_special': forms.TextInput(attrs={'class':'form-control', 'placeholder':'eg. 100'}),
		'areas': MultipleChoiceWidget('AreaAutocomplete', attrs={'class':'form-control', 'placeholder':'eg. Dubai Marina, JLT'}),
		'area_info': forms.TextInput(attrs={'class':'form-control', 'placeholder':'eg. Marina Pinnacle, near Marina Walk'}),
		}
		
	def clean(self):
		cleaned_data = super(NewCookProfileForm, self).clean()
		is_regular = cleaned_data.get('is_regular')
		price_regular = cleaned_data.get('price_regular')
		is_special = cleaned_data.get('is_special')
		price_special = cleaned_data.get('price_special')

		if (is_special or is_regular) == False:
			# msg = "You must select atleast one; Regular cooking or Special cooking"
			# self.add_error('is_regular', msg)
			# self.add_error('is_special', msg)
			
			raise forms.ValidationError("Please choose if you are a Regular or Special cook")

		elif is_special and not price_special:
		# 	msg = "Please enter a price for your special cooking services"
		# 	self.add_error('price_special', msg)
			raise forms.ValidationError("Please enter a price for your special cooking service")

		elif is_regular and not price_regular:
		# 	msg = "Please enter a price for your regular cooking services"
		# 	self.add_error('price_regular', msg)
			raise forms.ValidationError("Please enter a price for your regular cooking service")
		return cleaned_data


class MealForm(forms.ModelForm):
	class Meta:
		model = Meal
		exclude = ['cook',]
		widgets = {
		'image': ImageWidget(),
		}


class CookSearchForm(forms.Form):
	area = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter area to search..', 'label':""}))


class EmailForm(forms.Form):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Enter your email'}))
	message = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))


