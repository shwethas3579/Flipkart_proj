from django.db import models
from datetime import datetime

from customers.models import Customer
from products.models import Product


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now())
    amount = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
