"""Urls for this app"""

from django.urls import path
from dine_backend.views import DinnerView, DinnersAllView

urlpatterns = [
    path('', DinnersAllView.as_view()),
    path('<int:pk>/', DinnerView.as_view())
    # Uses the primary key of the database object (pk) to locate a single Dinner
]
