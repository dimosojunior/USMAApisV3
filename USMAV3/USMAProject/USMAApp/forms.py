from .models import *
from django import forms
from django.forms import ModelForm

class InformUsersForm(forms.ModelForm):


    class Meta:
        model = InformUsers
        fields ='__all__'