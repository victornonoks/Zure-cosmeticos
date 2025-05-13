from django.shortcuts import render
from .models import Produto
from django.http import HttpResponse
from django.contrib.auth.models import User

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
    if request.method == 'GET':  
        return render(request, 'zure_app/account-cadastro.html')
    else:
        name = request.POST.get('name')
        email = request.POST.get('email')
        telefone = request.POST.get('phone')
        senha = request.POST.get('password')
        senha2 = request.POST.get('confirm-password')

        email_exite = User.objects.filter(email=email).exists()

        if email_exite:
            return HttpResponse("Email já cadastrado")
        
        user = User.objects.create_user(username=name, email=email, password=senha)
        user.save()
        return HttpResponse('Cadastro realizado com sucesso!')

def login(request):
    return render(request, 'zure_app/account-login.html')

def carrinho (request):
    return render(request, 'zure_app/carrinho.html')