from django import forms

from cooks.models import Cook

class NewCookProfileForm(forms.ModelForm):
	class Meta:
		model = Cook
		exclude=['user']

class CookSearchForm(forms.Form):
	area = forms.CharField()