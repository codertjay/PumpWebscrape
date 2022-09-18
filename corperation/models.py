from django.db import models


# Create your models here.
class Cooperating(models.Model):
    """
    The cooperating model which is used in creating the api
    """
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    pincode = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    description = models.TextField()
    timings = models.CharField(max_length=250)
