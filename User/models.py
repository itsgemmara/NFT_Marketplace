from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager


class Profile(AbstractUser):

    username = None
    email = models.EmailField('email', unique=True, blank=True, null=True)
    phone_number = models.CharField('phone number', max_length=11, unique=True, blank=True, null=True)
    number_of_user_blocking = models.IntegerField(default=0, null=True)
    number_of_IP_blocking = models.IntegerField(default=0, null=True)
    is_locked = models.BooleanField(default=False)
    email_is_verified = models.BooleanField(default=False)
    phone_number_is_verified = models.BooleanField(default=False)
    user_is_deleted = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
