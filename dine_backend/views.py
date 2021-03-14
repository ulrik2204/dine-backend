"""The representation and method of the API"""

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from dine_backend.serializers import AllergySerializer, DinnerSerializer, RegistrationSerializer, UserSerilizer
from dine_backend.models import Allergy, Dinner, User


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


class AllergiesAllView(generics.ListAPIView):
    """The view for all Allergies class"""
    queryset = Allergy.objects.all()
    serializer_class = AllergySerializer


class AllergyView(generics.RetrieveAPIView):
    """The view for a single Allergy"""
    queryset = Allergy.objects.all()
    serializer_class = AllergySerializer


class UserListView(generics.ListAPIView):
    """The view for getting all users"""
    queryset = User.objects.all()
    serializer_class = UserSerilizer


class UserDetailView(generics.RetrieveAPIView):
    """The view for a single user"""
    queryset = User.objects.all()
    serializer_class = UserSerilizer


@api_view(['POST', ])
def registration_view(request):
    """The post request view to registrate a user"""
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'Successfully registered a new user'
            data['username'] = user.username
        else:
            data = serializer.errors
        return Response(data)
