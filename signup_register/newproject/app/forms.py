from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    email= forms.EmailField()
    phone_no=forms.CharField(max_length=20)
    first_name=forms.CharField(max_length=20)
    last_name=forms.CharField(max_length=20)
    class meta:
        model=User
        fields=['username','phone_no','email','password1','password2']

