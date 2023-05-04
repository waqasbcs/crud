from django.core import validators
from django import forms
from.models import user

class studentregistration(forms.ModelForm):
    class Meta: 
        model=user
        fields= ['name','email','password']
        widgets={
            'name':forms.TextInput(attrs={'class':'special','placeholder':'Enter your name'}),
            'email':forms.EmailInput(attrs={'class':'special','placeholder':'Enter your email'}),
            'password':forms.PasswordInput(render_value=True,attrs={'class':'special','placeholder':'Enter your password'}),
        
        }