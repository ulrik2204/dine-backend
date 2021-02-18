"""Serializers for the database models"""
from rest_framework import serializers
from dine_backend.models import Dinner


class DinnerSerializer(serializers.ModelSerializer):
    """Serializer for the dinner model"""
    class Meta:
        """Meta serializer"""
        model = Dinner
        fields = ("id", "dish", "cuisine", "date", "location", "owner")
