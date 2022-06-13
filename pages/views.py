from django.shortcuts import redirect, render
from django.http import HttpResponse
from.form import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages

def sign(request):
  if request.method=="POST":
        first=request.POST['first_name']
        last=request.POST['last_name']
        email=request.POST['email']
        passd=request.POST['password']
        messages.success(request, '')
        try:
          myuser=User.objects.create_user(email,email,passd)
        except:
            return HttpResponse("faaaaaaaaaaute")
        myuser.first_name=first
        myuser.last_name=last
        myuser.save()
        return redirect('login')
  return render(request,'signin.html',{'forme': form_login,'message': messages})

def login_com(request):
      if request.method=="POST":
        usern=request.POST['email']
        password=request.POST['password']
        user=authenticate(request,username=usern,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
      return render(request,'authenticate/login.html',{'forme':form_login})

def logout_com(request):
    logout(request)
    return redirect('login')