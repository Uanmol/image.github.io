from typing import Counter
from django.forms import fields
from django.http import request
from django.shortcuts import render
from .form import ImageForm
from .models import Image
from .models import Login
from django.contrib.auth.forms import AdminPasswordChangeForm, UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login , logout
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    if request.method =="POST":
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    img = Image.objects.all()
    no = 0
    for i in range(0,10):
        no = no + i
    return render(request,'index.html',{'img':img,'form':form,'no':no})

def signup(request):
    if request.method=="POST":
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
        return render(request,'signup.html',{'form':fm})
    else:
        fm = UserCreationForm()
        return render(request,'signup.html',{'form':fm})

def login(request):
    if request.method=="POST":
        fm = AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username= uname,password=upass)
            if user is not None:
                # login(request.user)
                return HttpResponseRedirect('/home/')
    else:
        fm = AuthenticationForm()
        return render(request,'login.html',{'form':fm})

def blog(request):
    return render(request,'blog.html')

def like(request):
    no = 1
    return HttpResponseRedirect('/home/')