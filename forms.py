from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Background



class SignUPForm(UserCreationForm):
    
    class Meta:
          model = User 
          fields = ['username', 'password1', 'password2', 'email']


class LoginForm(forms.Form):
     username = forms.CharField()
     password = forms.CharField(widget=forms.PasswordInput)


