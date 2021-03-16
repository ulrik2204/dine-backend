"""The representation and method of the API"""

from django.forms.models import model_to_dict
from rest_framework import generics
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, SAFE_METHODS
from rest_framework.response import Response
from dine_backend.serializers import AllergySerializer, DinnerSerializer, DinnerSignUpSerializer, RegistrationSerializer, UserSerializer
from dine_backend.models import Allergy, Dinner, User


class DinnersAllView(generics.ListCreateAPIView):
    """
    The view for the all dinners.
    Generics model already has GET, POST and HEAD method
    """
    queryset = Dinner.objects.all()
    serializer_class = DinnerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        if 'owner' in request.data:
            request.data.pop('owner')
        request.data['owner'] = request.user.id
        return super().post(request, *args, **kwargs)


class ReadOrIsDinnerOwner(BasePermission):
    """Permission class to check if it should read or else if the user is the owner"""

    def has_object_permission(self, request, view, dinner_obj):
        """A user has always permission read, but only to change the object if the user owns it"""
        # If it is a GET, OPTION or HEAD (a safe method) request, it is ok
        if request.method in SAFE_METHODS:
            return True
        # If it is a PATCH of PUT request, the user has to be the owner
        return dinner_obj.owner.id == request.user.id


class DinnerView(generics.RetrieveAPIView):
    """
    The view for a single dinner by their primary key in the databse
    """
    queryset = Dinner.objects.all()
    serializer_class = DinnerSerializer
    permission_classes = [AllowAny]


class AllergiesAllView(generics.ListAPIView):
    """The view for all Allergies class"""
    queryset = Allergy.objects.all()
    serializer_class = AllergySerializer
    permission_classes = [AllowAny]


class AllergyView(generics.RetrieveAPIView):
    """The view for a single Allergy"""
    queryset = Allergy.objects.all()
    serializer_class = AllergySerializer
    permission_classes = [AllowAny]


class UserListView(generics.ListAPIView):
    """The view for getting all users"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class UserDetailView(generics.RetrieveAPIView):
    """The view for a single user"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


@api_view(['POST', ])
@permission_classes([AllowAny, ])
def registration_view(request):
    """The post request view to registrate a user"""
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'Successfully registered a new user'
            data['username'] = user.username
            token = Token.objects.get(user=user).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)


@api_view(['PUT', ])
@permission_classes([IsAuthenticated, ])
def sign_up_for_dinner(request, pk):
    """The view for signing a user up for dinner"""
    try:
        dinnerContext = Dinner.objects.get(id=pk)
    except Dinner.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = DinnerSerializer(
            data=DinnerSerializer(dinnerContext).data)
        data = {}
        if serializer.is_valid():
            serializer.append_user(dinnerContext, request.user.id)
            data['success'] = 'Successfully signed up user for dinner'
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
