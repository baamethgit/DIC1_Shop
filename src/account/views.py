from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model,login,logout,authenticate
from .forms import signupForm,LoginForm
from datetime import datetime

User = get_user_model()

def convert_date_format(date_str):
    date_obj = datetime.strptime(date_str, '%d/%m/%Y')
    formatted_date = date_obj.strftime('%Y-%m-%d')
    return formatted_date

def signup_login_view(request):
    message = ''
    signup_form = signupForm()
    login_form = LoginForm()
    default_section = 'login'
    if request.method == 'POST':
        # Si le formulaire d'inscription est soumis
        if 'signup_form' in request.POST:
            default_section = 'signup'
            signup_form = signupForm(request.POST)
            if signup_form.is_valid():
                user = signup_form.save()
                login(request, user)
                return redirect('home-view')
            message = 'Informations invalides'
            context = {'signup_form': signup_form,'login_form': login_form,'login_message': "",'signup_message':message,"default_section":default_section}
            return render(request, 'account/signin.html', context=context)    
        # Si le formulaire de connexion est soumis
        elif 'login_form' in request.POST:
            default_section = 'login'
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                user = authenticate(
                    username=login_form.cleaned_data['username'],
                    password=login_form.cleaned_data['password'],
                )
                if user is not None:
                    login(request, user)
                    message = "utilisateur connecté avec succés"
                    print(message)
                    return redirect('home-view')
            message = 'Identifiants invalides.'
            context = {'signup_form': signup_form,'login_form': login_form,'login_message': message,'signup_message':"","default_section":default_section}
            return render(request, 'account/signin.html', context=context)
    context = {'signup_form': signup_form, 'login_form': login_form,'default_section':default_section}
    return render(request, 'account/signin.html', context=context)


class updateUser():
    pass
    # return render(request)

def stp1(request):
    if request.method == 'POST':
        # Si le formulaire d'inscription est soumis
        if 'signup_form' in request.POST:
            default_section = 'signup'
            signup_form = signupForm(request.POST)
            if signup_form.is_valid():
                # Stocker les informations saisies dans la session
                request.session['signup_data'] = signup_form.cleaned_data
                return redirect('step_two')  # Rediriger vers la deuxième étape d'inscription
            
            message = 'Informations invalides'
            context = {'signup_form': signup_form, 'login_form': 'login_form', 'login_message': '', 'signup_message': message, "default_section": default_section}
            return render(request, 'account/signin.html', context=context)