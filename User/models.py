from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager


class Profile(AbstractUser):

    username = None
    email = models.EmailField('email', unique=True, blank=True, null=True)
    phone_number = models.CharField('phone number', max_length=11, unique=True, blank=True, null=True)
    email_is_verified = models.BooleanField(default=False)
    phone_number_is_verified = models.BooleanField(default=False)
    user_is_deleted = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.phone_number if self.phone_number else self.email
