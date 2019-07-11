from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.TextField()
    price = models.FloatField()
    description = models.TextField(default = 'this is a product')

class Customer(models.Model):
    firstname = models.TextField()
    middlename = models.TextField()
    lastname = models.TextField()
    email = models.TextField()
    phone = models.TextField()
    description = models.TextField(default = 'this is a csutomer')