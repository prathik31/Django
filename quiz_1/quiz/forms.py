from django.forms import ModelForm
from .models import *
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from django import forms


class orderform(ModelForm):
    class Meta:
        model=profile
        fields='__all__'
