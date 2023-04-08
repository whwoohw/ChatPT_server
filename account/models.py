from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    SEX = (('male', 'male'), ('female', 'female'))

    age = models.IntegerField(null=True, blank=True)
    sex = models.CharField(max_length=10, choices = SEX, null=True, blank=True)

    def __str__(self):
        return f'{self.username}'