from allauth.account.forms import SignupForm
from django import forms
from .models import User

class CustomSignupForm(SignupForm):
    nome_completo = forms.CharField(max_length=150, label='Nome Completo')
    telefone = forms.CharField(max_length=20, required=False, label='Telfeone(opcional)')

    def save(self, request):
        user = super().save(request)
        user.nome_completo = self.cleaned_data['nome_completo']
        user.telefone = self.cleaned_data['telefone']
        user.save()
        return user
    