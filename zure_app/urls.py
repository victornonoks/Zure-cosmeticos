from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('destaque/', views.destaque1, name='destaque'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('carrinho/', views.carrinho, name='carrinho'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
