from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')

    phone = models.CharField(max_length=35, verbose_name='номер телефона', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    country = models.CharField(max_length=100, verbose_name='страна', **NULLABLE)

    email_token = models.CharField(max_length=20, verbose_name='токен', **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name='is_active')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
