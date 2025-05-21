from django.contrib.auth.models import AbstractUser
from django.db import models

class User (AbstractUser):
    full_name = models.CharField('Nome Completo', max_length=255)
    phone = models.CharField('Telefone', max_length=20, blank=True, null=True)

    def __str__(self):
        return self.email or self.username