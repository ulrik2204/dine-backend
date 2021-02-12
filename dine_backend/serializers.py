from rest_framework import serializers
from .models import Dinner

class DinnerSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Dinner
        fields = ("id", "dish", "cuisine", "date", "location", "owner")

