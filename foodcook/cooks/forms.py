from django import forms

from cooks.models import Cook, Area

class NewCookProfileForm(forms.ModelForm):
	class Meta:
		model = Cook
		widgets = {
		'neighbourhood': forms.TextInput(attrs={'rows':1, 'default':None}),
		}
		exclude=['user']



class CookSearchForm(forms.Form):
	area = forms.CharField()

	