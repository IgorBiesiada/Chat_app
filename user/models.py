import random
from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework import serializers


# Create your models here.

class User(AbstractUser):
    auth_code = models.CharField(max_length=6, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.auth_code:
            self.auth_code = f'{random.randint(100000, 999999)}'
        super().save(*args, **kwargs)
