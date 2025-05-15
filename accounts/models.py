from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    nome_completo = models.CharField(max_length=150)
    telefone = models.CharField(max_length=50, blank=True, null=True)    
