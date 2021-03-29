"""The representation and method of the API"""

from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import (SAFE_METHODS, AllowAny, BasePermission,
                                        IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from rest_framework.views import APIView

from dine_backend.models import Allergy, Dinner, User
from dine_backend.serializers import (AllergySerializer, DinnerSerializer,
                                      RegistrationSerializer, UserSerializer)


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


class DinnerView(generics.RetrieveUpdateAPIView):
    """
    The view for a single dinner by their primary key in the databse
    """
    queryset = Dinner.objects.all()
    serializer_class = DinnerSerializer
    permission_classes = [ReadOrIsDinnerOwner]


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
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserByTokenView(APIView):
    """The view to get a single user by their token"""
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """The get method to get a user by their token"""
        data = {}
        data['user'] = UserSerializer(request.user).data
        return Response(data, status=status.HTTP_200_OK)


@api_view(['POST', ])
@permission_classes([AllowAny, ])
def registration_view(request):
    """The post request view to registrate a user"""
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        boo = serializer.is_valid()
        if boo:
            user = serializer.save()
            data['response'] = 'Successfully registered a new user'
            data['username'] = user.username
            token = Token.objects.get(user=user).key
            data['token'] = token
            # This should be 201, but the frontend is not updated for that
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', ])
@permission_classes([IsAuthenticated, ])
def sign_up_for_dinner(request, pk):
    """The view for signing a user up for dinner"""
    try:
        dinner_context = Dinner.objects.get(id=pk)
    except Dinner.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        dinner_context_data = DinnerSerializer(dinner_context).data
        serializer = DinnerSerializer(
            data=dinner_context_data)
        data = {}
        if serializer.is_valid():
            if dinner_context.owner.id == request.user.id:
                data['detail'] = 'Cannot sign up an owner of a dinner event to its own dinner event'
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            serializer.append_user(dinner_context, request.user.id)
            data['success'] = 'Successfully signed up user for dinner'
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
