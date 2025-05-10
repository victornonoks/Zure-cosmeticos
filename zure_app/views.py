from django.shortcuts import render
from .models import Produto

def home(request):
    destaques = Produto.objects.filter(destaques=True)[:4]
    return render(request, 'zure_app/home.html', {'destaques': destaques})

def destaque1(request):
    return render(request, 'zure_app/destaque1.html')

def destaque2(request):
    return render(request, 'zure_app/destaque2.html')

def destaque3(request):
    return render(request, 'zure_app/destaque3.html')

def destaque4(request):
    return render(request, 'zure_app/destaque4.html')

def cadastro(request):
    return render(request, 'zure_app/account-cadastro.html')

def login(request):
    return render(request, 'zure_app/account-login.html')

def carrinho (request):
    return render(request, 'zure_app/carrinho.html')