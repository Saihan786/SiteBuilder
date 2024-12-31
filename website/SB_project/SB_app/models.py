from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal


class Site(models.Model):
    name = models.CharField(max_length=40, unique=True)
    area = models.DecimalField(
        max_digits=10,
        decimal_places=4,
        validators=[MinValueValidator(Decimal('0.0000'))],
    )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

class HouseTypes(models.Model):
    # add validators and testing in general here

    name = models.CharField(max_length=40, unique=True)
    configuration = models.CharField(max_length=40, unique=True)

    beds = models.IntegerField()
    storeys = models.IntegerField()
    sales_sq_ft = models.DecimalField(
        max_digits=10,
        decimal_places=4,
        validators=[MinValueValidator(Decimal('0.0000'))],
    )
    build_sq_ft = models.DecimalField(
        max_digits=10,
        decimal_places=4,
        validators=[MinValueValidator(Decimal('0.0000'))],
    )
    build_cost = models.DecimalField(
        max_digits=10,
        decimal_places=4,
        validators=[MinValueValidator(Decimal('0.0000'))],
    )
    build_cost_divide_sq_ft = models.DecimalField(
        max_digits=10,
        decimal_places=4,
        validators=[MinValueValidator(Decimal('0.0000'))],
    )
    build_weeks = models.IntegerField()
    depth = models.DecimalField(
        max_digits=10,
        decimal_places=4,
        validators=[MinValueValidator(Decimal('0.0000'))],
    )
    width = models.DecimalField(
        max_digits=10,
        decimal_places=4,
        validators=[MinValueValidator(Decimal('0.0000'))],
    )
    NDSS = models.BooleanField()
    NDSS_Description = models.CharField(max_length=40, unique=True)
    Accessibility = models.CharField(max_length=40, unique=True)
    parking_spaces = models.DecimalField(
        max_digits=10,
        decimal_places=4,
        validators=[MinValueValidator(Decimal('0.0000'))],
    )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
