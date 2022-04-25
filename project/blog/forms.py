from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        # fields = '__all__'
        fields = ('title', 'content', 'photo', 'category', 'published')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nomi'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Matni'
            }),
            'published': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select',
            }),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Foydalanuvchi ismi',
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control'
                               }))
    password = forms.CharField(label='Parol',
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                               }))



class RegistrationForm(UserCreationForm):

    username = forms.CharField(max_length=150, help_text='Maksimum 150 ta simvol',
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Foydalanuvchi ismi',
                                   'style': 'margin: 20px; width: 300px;'
                               }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Parol',
        'style': 'margin: 20px; width: 300px;'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Parolni tasdiqlang',
        'style': 'margin: 20px; width: 300px;'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email',
        'style': 'margin: 20px; width: 300px;'
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')