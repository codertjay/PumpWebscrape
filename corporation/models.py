from django.db import models


# Create your models here.
class Corporation(models.Model):
    """
    The Corporation  model which is used in creating the api
    """
    name = models.CharField(max_length=250, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    phone = models.CharField(max_length=250, blank=True, null=True)
    open_hours = models.CharField(max_length=250, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
