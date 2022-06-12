from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from.form import *

def sign(request):
    if request.method=="POST":
       form_login(request.POST).save(commit=True)
       return redirect("login")
    return render(request,'signin.html',{'forme': form_login})

def login(request):
    return render(request,'login.html',{'forme':form_login})
