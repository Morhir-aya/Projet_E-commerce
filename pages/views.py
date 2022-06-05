from django.shortcuts import render

def sign(request):
    return render(request,'signin.html')

def login(request):
    return render(request,'login.html')

