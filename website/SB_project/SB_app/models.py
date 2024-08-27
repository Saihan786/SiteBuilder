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