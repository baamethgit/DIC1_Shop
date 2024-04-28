
from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model,login,logout,authenticate
from .forms import CustomUserCreationForm,signupForm
User=get_user_model()

def login_user(request):
    if request.method == 'POST':
        courriel = request.POST.get("username")
        password = request.POST.get("password")
        print(courriel,password)
        user = authenticate(request, courriel=courriel, password=password)
        print(user)
        if user:
            login(request, user)
            return redirect('home-view')
    return render(request, "account/signin.html")


def signup_user(request):
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home-view')
    else:
        form = signupForm()
        # print(form)
    return render(request, 'account/signin.html', {'form': form})
