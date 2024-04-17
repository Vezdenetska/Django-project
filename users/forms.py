from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label='Wprowadź adres email',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wprowadź adres email'})
    )
    username = forms.CharField(
        label='Wprowadź login',
        required=True,
        help_text='Proszę nie używać symboli: @, /, _',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wprowadź login'})
    )
  
    password1 = forms.CharField(
        label='Wprowadź hasło',
        required=True,
        help_text='Hasło nie może być zbyt krótkie lub proste',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Wprowadź hasło'})
    )
    password2 = forms.CharField(
        label='Powtórz hasło',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Powtórz hasło'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        label='Wprowadź adres email',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wprowadź adres email'})
    )
    username = forms.CharField(
        label='Wprowadź login',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wprowadź login'})
    )

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileImageForm(forms.ModelForm):
    img = forms.ImageField(
        label='Wybierz zdjęcie profilowe',
        required=False,
        widget=forms.FileInput
        )
    class Meta:
        model = Profile
        fields = ['img']


class UserChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='Wprowadź stare hasło',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Wprowadź stare hasło'})
    )
    new_password1 = forms.CharField(
        label='Wprowadź nowe hasło',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Wprowadź nowe hasło'})
    )
    new_password2 = forms.CharField(
        label='Powtórz nowe hasło',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Powtórz nowe hasło'})
    )

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']