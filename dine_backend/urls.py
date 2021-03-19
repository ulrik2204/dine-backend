"""Urls for this app"""

from django.urls import path
from dine_backend.views import AllergiesAllView, AllergyView, DinnerView, DinnersAllView

urlpatterns = [
    path('dinners/', DinnersAllView.as_view()),
    path('dinners/<int:pk>/', DinnerView.as_view()),
    # Uses the primary key of the database object (pk) to locate a single Dinner
    path('allergies/', AllergiesAllView.as_view()),
    path('allergies/<int:pk>/', AllergyView.as_view())
]
