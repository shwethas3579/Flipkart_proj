from datetime import datetime

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.IntegerField()
    created_at = models.DateTimeField(default=datetime.now())

