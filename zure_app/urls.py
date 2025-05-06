from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('destaque1/', views.destaque1, name='destaque1'),
    path('destaque2/', views.destaque2, name='destaque2'),
    path('destaque3/', views.destaque3, name='destaque3'),
    path('destaque4/', views.destaque4, name='destaque4'),
]
