from django import forms

class SiteForm(forms.Form):
    name = forms.CharField(max_length=40)
    area = forms.DecimalField(max_digits=10, decimal_places=4)