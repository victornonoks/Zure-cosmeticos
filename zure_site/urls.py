"""
URL configuration for zure_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('destaque1/', views.destaque1, name='destaque1'),
    path('destaque2/', views.destaque2, name='destaque2'),
    path('destaque3/', views.destaque3, name='destaque3'),
    path('destaque4/', views.destaque4, name='destaque4'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('carrinho/', views.carrinho, name='carrinho'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

