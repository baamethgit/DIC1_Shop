from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserModel
from django.forms import ModelForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("courriel",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields = ("courriel",)
        
class signupForm(ModelForm):
    class Meta:
        model = UserModel
        fields = ('prenom','nom','courriel','date_naissance')