from django import forms
from .models import Customer, Flower

class PurchaseForm(forms.Form):
    customer = forms.ModelChoiceField(queryset=Customer.objects.all())
    flower = forms.ModelChoiceField(queryset=Flower.objects.all())

class CustomerForm(forms.Form):
    customer = forms.ModelChoiceField(queryset=Customer.objects.all())
