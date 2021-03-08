"""Database models for dine"""
from django.db import models


class Allergy(models.Model):
    """Model for an allergy"""
    allergy = models.CharField(max_length=50, null=False)


class Dinner(models.Model):
    """The dinner model"""
    dish = models.CharField(max_length=50, null=False)
    cuisine = models.CharField(max_length=50, null=False)
    date = models.DateTimeField(null=False)
    location = models.CharField(max_length=100, null=False)
    owner = models.CharField(max_length=50, null=False)
    description = models.TextField(null=False, default="")
    allergies = models.ManyToManyField(Allergy, blank=True)
