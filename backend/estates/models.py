from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Estate(models.Model):
    title = models.CharField(max_length=140)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=13, decimal_places=2)
    image = models.ImageField(blank=True)
