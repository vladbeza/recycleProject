from django import forms

class CuponForm(forms.Form):
    code = forms.CharField()
