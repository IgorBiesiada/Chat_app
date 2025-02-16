from random import random

from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework import serializers


# Create your models here.

class User(AbstractUser):
    auth_code = models.CharField(max_length=6, unique=True, null=True)

    def generate_auth_code(self):
        self.auth_code = f'{random.randint(100000, 999999)}'
        self.save()



