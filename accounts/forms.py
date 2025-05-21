from django import forms
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    full_name = forms.CharField(
        max_length=150,
        label="Nome completo",
        widget=forms.TextInput(attrs={'placeholder': 'Seu nome completo'}),
        required=True
    )
    phone = forms.CharField(
        max_length=20,
        label="Telefone",
        widget=forms.TextInput(attrs={'placeholder': '(00) 00000-0000'}),
        required=False
    )

    def save(self, request):
        user = super().save(request)
        user.full_name = self.cleaned_data['full_name']
        user.phone     = self.cleaned_data['phone']
        user.save()
        return user