from django.db import models
from django.contrib.auth.models import User


#Create your model here.
class Customer(models.Model):
    user = models.OneToOneField( User , on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city =models.CharField(max_length=20, blank=True, null=True)
    country= models.CharField(max_length=200, blank=True, null=True)
    joined_at =models.DateTimeField(auto_now_add=True)


def __str__(self):
     return self.user.username


