#  model: schema of a table
from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mobile = models.IntegerField()
    email = models.CharField(max_length=255)
    dob = models.DateTimeField()
    address = models.TextField(max_length=255)
    age = models.IntegerField(default=1)
    father_name = models.CharField(max_length=255, default='Father')
    # address = models.ForeignKey(Address, on_delete=models.CASCADE)

# obj = Customer()
# print(obj.age)