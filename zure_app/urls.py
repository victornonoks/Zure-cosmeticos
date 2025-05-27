from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('carrinho/', views.carrinho, name='carrinho'),
    path('produtos/', views.produtos, name='produtos'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('produto/<slug:slug>', views.destaque, name='destaque')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
