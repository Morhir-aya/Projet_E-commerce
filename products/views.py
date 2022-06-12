from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def blog(request):
    return render(request,'blog-grid.html')

def faq(request):
    return render(request,'faq.html')

def dash(request):
    return render(request,'dashboard.html')

def order(request):
    return render(request,'order.html')

def address(request):
    return render(request,'address.html')

def profild(request):
    return render(request,'profile-details.html')

def Checkout(request):
    return render(request,'Checkout.html')

def cart(request):
    return render(request,'cart.html')

def confirm(request):
    return render(request,'confirmation.html')

def prodd(request):
    return render(request,'product-single.html')

def shopsb(request):
    return render(request,'shop-sidebar.html')

def purchaseconf(request):
    return render(request,'purchase-confirmation.html')