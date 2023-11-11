from django import forms
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    email = forms.EmailField(label='E-Posta Adresiniz', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Şifreniz', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    remember_me = forms.BooleanField(required=False, initial=True, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

class RegistrationForm(forms.Form):
    first_name = forms.CharField(
        label='Adınız',
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control w-100'}),
        required=True,
    )
    last_name = forms.CharField(
        label='Soyadınız',
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    email = forms.EmailField(
        label='E-Posta Adresiniz',
        max_length=40,
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=True
    )
    password = forms.CharField(
        label='Şifreniz',
        min_length=8,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True
    )
    confirm_password = forms.CharField(
        label='Şifrenizi Onaylayın',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True
    )
    company = forms.CharField(
        label='Şirketiniz',
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )
    position = forms.CharField(
        label='Pozisyonunuz',
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise ValidationError("Şifreler eşleşmiyor. Lütfen aynı şifreyi girin.")
