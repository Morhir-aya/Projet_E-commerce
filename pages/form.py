from dataclasses import field
from django import forms
from matplotlib import widgets
from .models import *

class form_login(forms.ModelForm):
    class Meta:
        model=user
        fields=('first_name','last_name','username','email','password')
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),
            'email':forms.TextInput(attrs={'type':'email','class':'form-control','placeholder':'Email'}),
            'password':forms.TextInput(attrs={'type':'password','class':'form-control','placeholder':'Password'}),
        }