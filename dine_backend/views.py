"""The representation and method of the API"""

from rest_framework import generics
from dine_backend.serializers import AllergySerializer, DinnerSerializer
from dine_backend.models import Allergy, Dinner


class DinnersAllView(generics.ListCreateAPIView):
    """
    The view for the all dinners.
    Generics model already has GET, POST and HEAD method
    """
    queryset = Dinner.objects.all()
    serializer_class = DinnerSerializer


class DinnerView(generics.RetrieveAPIView):
    """
    The view for a single dinner by their primary key in the databse
    """
    queryset = Dinner.objects.all()
    serializer_class = DinnerSerializer


class AllergiesAllView(generics.ListCreateAPIView):
    """The view for all Allergies class"""
    queryset = Allergy.objects.all()
    serializer_class = AllergySerializer


class AllergyView(generics.RetrieveAPIView):
    """The view for a single Allergy"""
    queryset = Allergy.objects.all()
    serializer_class = AllergySerializer
