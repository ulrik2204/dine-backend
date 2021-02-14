"""Urls for this app"""

from django.urls import path
from .views import DinnerView

urlpatterns = [
    path('', DinnerView.as_view())
]
