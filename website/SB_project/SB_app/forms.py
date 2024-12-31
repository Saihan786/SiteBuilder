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

class HouseTypeForm(forms.Form):
    # add validators and testing in general here

    name = forms.CharField(max_length=40)
    configuration = forms.CharField(max_length=40)

    beds = forms.IntegerField()
    storeys = forms.IntegerField()
    sales_sq_ft = forms.DecimalField(
        max_digits=10,
        decimal_places=4,
        validators=[MinValueValidator(Decimal('0.0000'))],
    )
    build_sq_ft = forms.DecimalField(
        max_digits=10,
        decimal_places=4,
        validators=[MinValueValidator(Decimal('0.0000'))],
    )
    build_cost = forms.DecimalField(
        max_digits=10,
        decimal_places=4,
        validators=[MinValueValidator(Decimal('0.0000'))],
    )
    build_cost_divide_sq_ft = forms.DecimalField(
        max_digits=10,
        decimal_places=4,
        validators=[MinValueValidator(Decimal('0.0000'))],
    )
    build_weeks = forms.IntegerField()
    depth = forms.DecimalField(
        max_digits=10,
        decimal_places=4,
        validators=[MinValueValidator(Decimal('0.0000'))],
    )
    width = forms.DecimalField(
        max_digits=10,
        decimal_places=4,
        validators=[MinValueValidator(Decimal('0.0000'))],
    )
    NDSS = forms.BooleanField()
    NDSS_Description = forms.CharField(max_length=40)
    Accessibility = forms.CharField(max_length=40)
    parking_spaces = forms.DecimalField(
        max_digits=10,
        decimal_places=4,
        validators=[MinValueValidator(Decimal('0.0000'))],
    )
