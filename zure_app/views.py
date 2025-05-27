from django.shortcuts import render, get_object_or_404
from .models import Produto

def home(request):
    destaques = Produto.objects.filter(destaques=True)[:4]
    produtos = Produto.objects.all()
    return render(request, 'zure_app/home.html', {'destaques': destaques, 'produtos': produtos})

def destaque(request, slug):
    produto = get_object_or_404(Produto, slug=slug)
    return render(request, 'zure_app/destaque.html', {'produto': produto})

def signup(request):
    return render(request, 'zure_app/signup.html')

def login(request):
    return render(request, 'zure_app/login.html')

def carrinho (request):
    return render(request, 'zure_app/carrinho.html')

def profile(request):
    return render(request, 'zure_app/profile.html')

def produtos(request):
    produtos = Produto.objects.all()
    for p in produtos:
        p.parcela = round(p.preco / 6, 2)
    return render(request, 'zure_app/produtos.html', {'produtos': produtos})