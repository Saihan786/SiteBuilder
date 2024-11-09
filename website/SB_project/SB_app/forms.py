from django import forms
from django.core.validators import MinValueValidator
from decimal import Decimal


class SiteForm(forms.Form):
    name = forms.CharField(max_length=40)
    area = forms.DecimalField(
        max_digits=10,
        decimal_places=4,
        validators=[MinValueValidator(Decimal('0.0000'))],
    )