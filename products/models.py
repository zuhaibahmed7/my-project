from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.CharField(max_length=2083)


class Offer(models.Model):
    code =models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()


    # in products/models.py OR core/models.py
#class ContactMessage(models.Model):
 #   name = models.CharField(max_length=255)
  #  email = models.CharField(max_length=255)
   # subject = models.CharField(max_length=255)
    #message = models.CharField(max_length=255)


