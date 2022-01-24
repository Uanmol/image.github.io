from typing import Match
from django.db import models

# Create your models here.
# class Category(models.Model):
#     title = models.CharField(max_length=20)
#     desc = models.TextField()

class Image(models.Model):
    photo = models.ImageField(upload_to="myimage")
    date = models.DateTimeField(auto_now_add=True)
    

class Login(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    def __str__(self):
        return self.name

