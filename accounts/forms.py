from django import forms
from .models import User
from allauth.account.forms import SignupForm

class CustomSignupForm(forms.Form):
    full_name = forms.CharField(
        max_length=255, 
        label='Nome completo'
        )
    phone = forms.CharField(
        max_length=20, 
        label='Telefone', 
        required=False
        )

    def signup(self, request, user):
        user.full_name = self.cleaned_data['full_name']
        user.phone = self.cleaned_data['phone']
        user.save()
        return user