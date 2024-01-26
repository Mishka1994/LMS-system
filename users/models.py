from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None

    email = models.EmailField(verbose_name='Почта', unique=True)
    first_name = models.CharField(max_length=100, verbose_name='Имя', **NULLABLE)
    last_name = models.CharField(max_length=100, verbose_name='Фамилия', **NULLABLE)
    phone = models.PositiveIntegerField(verbose_name='Телефон', **NULLABLE)
    city = models.CharField(max_length=256, verbose_name='Город', **NULLABLE)
    avatar = models.ImageField(upload_to='course/', verbose_name='Аватарка', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
