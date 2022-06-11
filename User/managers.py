from django.contrib.auth.models import BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, phone_number=None, email=None, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            email = None
        if not phone_number:
            phone_number = None
        if (not phone_number) and (not email):
            raise ValueError('The given phone or email must be set')
        user = self.model(phone_number=phone_number, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, email, password=None, **extra_fields):
        """Create and save a regular User with the given phone number and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone_number=phone_number, email=email, password=password, **extra_fields)

    def create_superuser(self, phone_number, password=None, **extra_fields):
        """Create and save a SuperUser with the given phone number and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser must have is_active=True.')
        return self._create_user(phone_number=phone_number,  password=password, **extra_fields)
