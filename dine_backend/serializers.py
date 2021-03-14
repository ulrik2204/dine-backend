"""Serializers for the database models"""
from rest_framework import serializers
from dine_backend.models import Allergy, Dinner, User


class DinnerSerializer(serializers.ModelSerializer):
    """Serializer for the dinner model"""
    class Meta:
        """Meta serializer"""
        model = Dinner
        fields = ("id", "dish", "cuisine", "date", "location",
                  "owner", "description", "allergies")


class AllergySerializer(serializers.ModelSerializer):
    """Serilizer for the allergy model"""
    class Meta:
        """Meta serializer"""
        model = Allergy
        fields = ("id", "allergy")


class UserSerilizer(serializers.ModelSerializer):
    """Serializer for the User model"""
    class Meta:
        """Meta class for UserSerilizer"""
        model = User
        fields = ("id", "username", "first_name",
                  "last_name", "address", "allergies", "about_me")


class RegistrationSerializer(serializers.ModelSerializer):
    """Serializer for registering a user"""

    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        """The meta class"""
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'address', 'password', "password2")
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        """Saving the user"""
        user = User(username=self.validated_data['username'], first_name=self.validated_data['first_name'],
                    last_name=self.validated_data['last_name'], address=self.validated_data['address'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        # Checking if the passwords match
        if password != password2:
            raise serializers.ValidationError(
                {'password': 'Passwords must match.'})

        user.set_password(password)
        user.save()
        return user
