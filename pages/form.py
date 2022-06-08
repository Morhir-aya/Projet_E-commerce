from dataclasses import field
from django import forms
from .models import *

class form_login(forms.ModelForm):
    class Meta:
        model=user
        fields=('nom','prenom','email',)