from django import forms
from .models import City

class CityForm(forms.Form):
    city = forms.ModelChoiceField(queryset=City.objects.all(), label="Select a city")
