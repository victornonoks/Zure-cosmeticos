from django.shortcuts import render
from .models import Produto

def home(request):
    destaques = Produto.objects.filter(destaques=True)[:4]
    produtos = Produto.objects.all()
    return render(request, 'zure_app/home.html', {'destaques': destaques, 'produtos': produtos})

def destaque1(request):
    return render(request, 'zure_app/destaque.html')

def signup(request):
    return render(request, 'zure_app/signup.html')

def login(request):
    return render(request, 'zure_app/login.html')

def carrinho (request):
    return render(request, 'zure_app/carrinho.html')

def produtos(request):
    produtos = Produto.objects.all()
    for p in produtos:
        p.parcela = round(p.preco / 6, 2)
    return render(request, 'zure_app/produtos.html', {'produtos': produtos})