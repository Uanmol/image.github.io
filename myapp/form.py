from django import forms
from django.db import models
from django.forms import fields
from .models import Image
from .models import Login

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['photo']

# class LoginForm(forms.ModelForm):
#     class Meta:
#         models = Login
#         fields = '__all__'
