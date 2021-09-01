from django.contrib.auth.models import AbstractUser
from django.db import models

from . import managers


class User(AbstractUser):
    username = None
    email = models.EmailField("email address", unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = managers.UserManager()

    def __str__(self):
        return self.email
