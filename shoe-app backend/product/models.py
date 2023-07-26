from django.db import models
from datetime import datetime

class Store(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Producer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    store = models.CharField(max_length=20,null=False, blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    producer = models.CharField(max_length=20,null=False, blank=False)
    def __str__(self):
        return self.name