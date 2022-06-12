from django.urls import path
from . import views

urlpatterns = [
  path('home/',views.home,name='home'),
  path('about/',views.about,name='about'),
  path('contact/',views.contact,name='contact'),
  path('blog/',views.blog,name='blog'),
  path('faq/',views.faq,name='faq'),
  path('dash/',views.dash,name='dash'),
  path('order/',views.order,name='order'),
  path('address/',views.address,name='address'),
  path('profild/',views.profild,name='profild'),
  path('Checkout/',views.Checkout,name='Checkout'),
  path('cart/',views.cart,name='cart'),
  path('confirm/',views.confirm,name='confirm'),
  path('prodd/',views.prodd,name='prodd'),
  path('shopsb/',views.shopsb,name='shopsb'),
  path('purchaseconf/',views.purchaseconf,name='purchaseconf'),
]