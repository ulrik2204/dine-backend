from django.shortcuts import render
from rest_framework import generics
from .serializers import DinnerSerializer
from .models import Dinner


class DinnerView(generics.CreateAPIView):
    queryset = Dinner.objects.all()
    serializer_class = DinnerSerializer
