"""Database models for dine"""
from django.db.models.manager import BaseManager
from dine.settings import AUTH_USER_MODEL
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Allergy(models.Model):
    """Model for an allergy"""
    allergy = models.CharField(max_length=50, null=False)


class MyUserManager(BaseUserManager):
    """Manager class for the User model"""
    # Requred methods to override

    def create_user(self, username, first_name, last_name, address, password=None):
        """Create the user"""
        # Check if required fields are there
        if not username:
            raise ValueError("Users must have a username")
        if not first_name:
            raise ValueError("Users must have a first name")
        if not last_name:
            raise ValueError("Users must have a last name")
        if not address:
            raise ValueError("Users must have a address")

        user = self.model(username=username, first_name=first_name,
                          last_name=last_name, address=address)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, address, password):
        """Create a superuser"""
        user = self.create_user(username, first_name,
                                last_name, address, password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    """The user model"""
    # The important user values
    username = models.CharField(max_length=100, unique=True, null=True)
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    address = models.CharField(max_length=100)
    allergies = models.ManyToManyField(Allergy, blank=True)
    about_me = models.TextField(default="")

    # Required fields for custom user
    date_joined = models.DateTimeField(
        verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(
        verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Set the fields
    USERNAME_FIELD = 'username'
    # Required fields
    REQUIRED_FIELDS = ['first_name', 'last_name', 'address']

    objects = MyUserManager()

    def __str__(self) -> str:
        return self.username

    # Required functions
    def has_perm(self, perm, obj=None):
        """Check if the user is an admin"""
        return self.is_admin

    def has_module_perms(self, app_label):
        """Check if the user has module permissions"""
        return True


@receiver(post_save, sender=AUTH_USER_MODEL)
def create_aut_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Dinner(models.Model):
    """The dinner model"""
    dish = models.CharField(max_length=50, null=False)
    cuisine = models.CharField(max_length=50, null=False)
    date = models.DateTimeField(null=False)
    location = models.CharField(max_length=100, null=False)
    owner = models.OneToOneField(
        User, null=False, on_delete=models.CASCADE, related_name='+')
    description = models.TextField(default="")
    allergies = models.ManyToManyField(Allergy, blank=True)
    signed_up_users = models.ManyToManyField(User, blank=True)

    class Meta:
        """Meta data for the Dinner Model"""
        # Order by the date the dinner will take place
        ordering = ['date']

    def sign_up_user(self, user):
        """Sign a user up for a dinner"""
        self.signed_up_users.add(user)
        return self
