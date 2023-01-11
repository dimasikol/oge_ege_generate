from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from .models import Profiles

class RegisterForm(UserCreationForm):
    email=forms.EmailField(required=True)

    class Meta:
        model=User
        fields=['username','email','password1','password2',]

class AccountAuthenticationForm(forms.Form):
    class Meta:
        models = User
        fields = ('username','password')



class RenameForm(UserChangeForm):
     email=forms.EmailField(required=True)
     class Meta:
         model = User
         fields = ['first_name','last_name','email']

# class RenameFormProfile(UserChangeForm):
#     email = forms.EmailField(required=True)
#     class Meta:
#         model = Profiles
#         exclude = ['user','password']

