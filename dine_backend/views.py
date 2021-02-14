"""The representation and method of the API"""

from rest_framework import generics
from .serializers import DinnerSerializer
from .models import Dinner


class DinnerView(generics.ListCreateAPIView):
    """
    The view for the dinner model.
    Generics model already has GET, POST and HEAD method
    """
    queryset = Dinner.objects.all()
    serializer_class = DinnerSerializer
