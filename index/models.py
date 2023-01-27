from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserObject(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin','admin'),
        ('manager','manager'),
        ('vendor','vendor'),
        ('customer', 'customer'),
    )
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=32, null=True)
    user_type = models.CharField(max_length=255, choices=USER_TYPE_CHOICES)
    