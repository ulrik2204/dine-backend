"""Urls for this app"""

from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from dine_backend.views import (AllergiesAllView, AllergyView, DinnersAllView,
                                DinnerView, UserByTokenView, UserDetailView, UserIsAdminView,
                                UserListView, registration_view,
                                sign_up_for_dinner)

app_name = 'dine_backend'

urlpatterns = [
    path('dinners/', DinnersAllView.as_view()),
    path('dinners/<int:pk>/', DinnerView.as_view()),
    # Uses the primary key of the database object (pk) to locate a single Dinner
    path('dinners/<int:pk>/signup/', sign_up_for_dinner, name='signup'),
    path('allergies/', AllergiesAllView.as_view()),
    path('allergies/<int:pk>/', AllergyView.as_view()),
    path('users/', UserListView.as_view()),
    path('users/<int:pk>/', UserDetailView.as_view()),
    path('users/getbytokenheader/', UserByTokenView.as_view()),
    path('users/isadmin/', UserIsAdminView.as_view()),
    path('users/register/', registration_view, name='register'),
    path('users/login/', obtain_auth_token, name='login'),
]
