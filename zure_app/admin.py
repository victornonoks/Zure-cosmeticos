from django.contrib import admin
from .models import Produto

#Registra o modelo Produto no admin do Django
admin.site.register(Produto)