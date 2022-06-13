from django.urls import path
from . import views

urlpatterns = [
  path('',views.login_com,name='login'),
  path('sign/',views.sign,name='signin'),
    path('logout/',views.logout_com,name='logout'),

]