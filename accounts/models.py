from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    last_activity = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
