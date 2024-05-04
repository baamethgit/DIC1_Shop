from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserModel
from django.forms import ModelForm
from django import forms
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
    username = forms.EmailField(max_length=63, label='Courriel',widget=forms.EmailInput(attrs={'class': 'field'}))
    password = forms.CharField(max_length=63, widget=forms.PasswordInput(attrs={'class': 'field'}),label='Password')    
    
class signupForm(ModelForm):
    class Meta:
        model = UserModel
        fields = ('prenom', 'nom', 'date_naissance', 'courriel')
        widgets = {
            'prenom': forms.TextInput(attrs={'class': 'field'}),
            'nom': forms.TextInput(attrs={'class': 'field'}),
            'courriel': forms.TextInput(attrs={'class': 'field'}),
            'date_naissance': forms.TextInput(attrs={'class': 'field', 'placeholder': 'JJ/MM/AAAA'})
        }

class updateForm(ModelForm):
    class Meta:
        model = UserModel
        fields = ('prenom','nom','courriel',"mail_secondaire",'telephone',"adresse",'pays','region','code_postal')
        widgets = {
            # 'mail_secondaire': forms.EmailField(),
            'telephone':forms.TextInput()
        }
        
class updatePasswordForm():
    pass