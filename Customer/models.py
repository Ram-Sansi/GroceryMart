from django.db import models
from Merchant.models import *


# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    dob = models.DateField()
    mobile = models.IntegerField()
    password = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=255)

    class Meta:
        db_table = 'client'

    def __str__(self):
        return self.name


class Cart(models.Model):
    quantity = models.FloatField()
    total_price = models.FloatField()
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)

    class Meta:
        db_table = 'addtocart'


class Bill(models.Model):
    totalprice = models.FloatField()
    totalitems = models.FloatField()
    billdate = models.DateField()
    billtime = models.TimeField()
    paymentstatus = models.CharField(max_length=1, choices=(("p", "pending"), ("c", "completed")), default='p')
    Client = models.ForeignKey(to=Client, on_delete=models.CASCADE)

    class Meta:
        db_table = 'bill'


class Billdetail(models.Model):
    itemprice = models.FloatField()
    quantity = models.FloatField()
    Product = models.ForeignKey(to=Products, on_delete=models.CASCADE)
    Bill = models.ForeignKey(to=Bill, on_delete=models.CASCADE)
    Client = models.ForeignKey(to=Client, on_delete=models.CASCADE)

    class Meta:
        db_table = 'billdetail'
