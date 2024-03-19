from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class orderform(ModelForm):
    class Meta:
        model=order
        fields='__all__'


class customerform(ModelForm):
    class Meta:
        model=customer
        fields='__all__'


class userform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']


class productform(ModelForm):
    class Meta:
        model=products
        fields='__all__'