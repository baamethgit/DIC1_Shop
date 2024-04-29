from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserModel
from django.forms import ModelForm
from django import forms
from django.forms.widgets import NumberInput  
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("courriel",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields = ("courriel",)
   
# authentication/forms.py
class LoginForm(forms.Form):
    username = forms.EmailField(max_length=63, label='Courriel')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Password')    
     
class signupForm(ModelForm):
    class Meta:
        model = UserModel
        fields = ('prenom','nom','courriel','date_naissance')
        widgets = {
            'date_naissance': forms.TextInput(attrs={'placeholder': 'JJ/MM/AAAA'})
        }