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
   
class LoginForm(forms.Form):
    username = forms.EmailField(max_length=63, label='Courriel',widget=forms.EmailInput(attrs={'class': 'field'}))
    password = forms.CharField(max_length=63, widget=forms.PasswordInput(attrs={'class': 'field password_input'}),label='Mot de passe')    
    
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
class signupFormStep2(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'field password_input','placeholder': 'Mot de passe'}), label='Mot de passe')
    password_confirmation = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'field password_input'}), label='Confirmation du mot de passe')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirmation = cleaned_data.get('password_confirmation')
        if password != password_confirmation:
            raise forms.ValidationError("Les mots de passe ne correspondent pas.")
        return cleaned_data
    
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