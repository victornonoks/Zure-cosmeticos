from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('destaque1/', views.destaque1, name='destaque1'),
    path('destaque2/', views.destaque2, name='destaque2'),
    path('destaque3/', views.destaque3, name='destaque3'),
    path('destaque4/', views.destaque4, name='destaque4'),
    path('carrinho/', views.carrinho, name='carrinho'),
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
