"""Urls for this app"""

from django.urls import path

from dine_backend.views import (AllergiesAllView, AllergyView, DinnersAllView,
                                DinnerView, UserDetailView, UserListView,
                                registration_view)

app_name = 'dine_backend'

urlpatterns = [
    path('dinners/', DinnersAllView.as_view()),
    path('dinners/<int:pk>/', DinnerView.as_view()),
    # Uses the primary key of the database object (pk) to locate a single Dinner
    path('allergies/', AllergiesAllView.as_view()),
    path('allergies/<int:pk>/', AllergyView.as_view()),
    path('users/', UserListView.as_view()),
    path('users/<int:pk>', UserDetailView.as_view()),
    path('users/register', registration_view, name='register')
]
