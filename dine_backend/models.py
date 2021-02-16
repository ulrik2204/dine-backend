"""Database models for dine"""
from django.db import models


class Dinner(models.Model):
    """The dinner model"""
    dish = models.CharField(max_length=50, null=False, default="")
    cuisine = models.CharField(max_length=50, null=False, default="Norwegian")
    date = models.DateTimeField(null=False)
    location = models.CharField(max_length=100, null=False)
    owner = models.CharField(max_length=50, null=False, default="")
