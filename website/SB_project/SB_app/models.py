from django.db import models

# Create your models here.
class Site(models.Model):
    name = models.CharField(max_length=40)
    area = models.DecimalField(max_digits=10, decimal_places=4)