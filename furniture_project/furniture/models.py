# furniture/models.py

from django.db import models

class Furniture(models.Model):
    furniture_name = models.CharField(max_length=255)
    furniture_type = models.CharField(max_length=255)
    features = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    material_used = models.CharField(max_length=255)

    def __str__(self):
        return self.furniture_name


class Customer(models.Model):
    customername = models.CharField(max_length=255)
    cphone = models.CharField(max_length=15)
    cemail = models.EmailField()
    purchase = models.ManyToManyField(Furniture, related_name='purchased_by')

    def __str__(self):
        return self.customername


class Supplier(models.Model):
    suppler_name = models.CharField(max_length=255)
    sphone = models.CharField(max_length=15)
    semail = models.EmailField()
    supply = models.ManyToManyField(Furniture, related_name='supplied_by')

    def __str__(self):
        return self.suppler_name
