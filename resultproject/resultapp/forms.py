from django import forms

class USNForm(forms.Form):
    usn = forms.CharField(max_length=10, label='Enter USN')
