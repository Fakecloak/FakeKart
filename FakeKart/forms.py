from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from pyexpat import model

# Create your forms here.

class CustomUserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter email address'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'}))
    class Meta:
        model=User
        fields=['username', 'email', 'password1', 'password2']
