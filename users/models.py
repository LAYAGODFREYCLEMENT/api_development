from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    wmail = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateField(default=timezone.now)

    USERNAME = "email"
    REQUIRED_FIELDS = []
