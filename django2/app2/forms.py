from django import forms
from app2.models import Bank

class InputForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = ['fname', 'lname', 'aadhar', 'pincode']
