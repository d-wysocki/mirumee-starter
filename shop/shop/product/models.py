from django.db import models


class Product(models.Model):
    name = models.CharField(null=False, blank=False, max_length=50)
    price = models.DecimalField(null=False, blank=False,decimal_places=2, max_digits=12)
    description = models.CharField(null=False, blank=False, max_length=255)
    quantity = models.IntegerField(default=0)