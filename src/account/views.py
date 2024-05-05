from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model,login,logout,authenticate
from account.models import UserModel
from .forms import signupForm,LoginForm,signupFormStep2
from datetime import datetime
from django.views.generic import UpdateView
import requests

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
                signup_data = signup_form.cleaned_data
                signup_data['date_naissance'] = signup_data['date_naissance'].strftime('%Y-%m-%d')
                request.session['signup_data_part1'] = signup_data 
                return redirect('signup_step2')
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


def signup_view_2(request):
    error = ''
    signup_data_part1 = request.session.get('signup_data_part1')
    if signup_data_part1:
        if request.method == 'POST':        
            signup_form_part2 = signupFormStep2(request.POST)
            if signup_form_part2.is_valid():
                password = signup_form_part2.cleaned_data['password']
                confirm_password = signup_form_part2.cleaned_data['password_confirmation']
                if password == confirm_password:
                    user = UserModel.objects.create_user(**signup_data_part1, password=password)
                    if user is not None:
                        del request.session['signup_data_part1']
                        login(request, user)
                        return redirect('home-view')
                else:
                    error = 'mots de passe différents'
                    return render(request, 'account/signup_partie2.html', {"error":error})
            print('form invalide',signup_form_part2.errors)
            return redirect('signup_step2')
        else:
            signup_form_part2 = signupFormStep2()
            return render(request, 'account/signup_partie2.html', {'form': signup_form_part2})
    return redirect('signup-login-view')

    
def updateUser(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('signup-login-view')
    countries_response = requests.get("https://restcountries.com/v3.1/all")
    if countries_response.status_code == 200:
        countries_data = countries_response.json()
        countries = [country['name']['common'] for country in countries_data]
        countries.sort()
    else:
        countries = ''
        
    context = {'user':user,'countries': countries}
    if request.method == 'POST':
        if 'param_compte' in request.POST:
            erreur = ''
            prenom_nom = request.POST.get('prenom_nom')
            courriel = request.POST.get('courriel')
            mail_secondaire = request.POST.get('mail_secondaire')
            telephone = request.POST.get('telephone')
            adresse = request.POST.get('adresse')
            pays = request.POST.get('pays')
            region = request.POST.get('region')
            code_postal = request.POST.get('code_postal')
            
            # mis a jour
            try:
                prenom, nom = prenom_nom.strip().rsplit(' ', 1)
                user.prenom = prenom
                user.nom = nom
            except:
                erreur = 'saisissez le nom et le prenom'
                user.prenom = prenom_nom
                user.nom = ''
            user.courriel = courriel
            user.mail_secondaire = mail_secondaire
            user.telephone = telephone
            user.adresse = adresse
            user.pays = pays
            user.region = region
            user.code_postal = code_postal
            if not erreur:
                user.save()
                login(request, user)
                return redirect("user_profil_view")
            else:
                context['erreur'] = erreur
                return render(request,'account/modifier_user.html',context) 
        if 'modifier_mot_de_passe' in request.POST:
            mdp_actuel = request.POST.get('mdp_actuel')
            new_mdp = request.POST.get('new_mdp')
            new_mdp_confirm = request.POST.get('new_mdp_confirm')
            if user.check_password(mdp_actuel):
                if new_mdp == new_mdp_confirm:
                    user.set_password(new_mdp)
                    user.save()
                    login(request, user)
                    return redirect("user_profil_view")
                else:
                    message_erreur = "Les nouveaux mots de passe ne correspondent pas."
            else:
                message_erreur = 'mot de passe actuel incorrect'
            context['message_erreur'] = message_erreur
            return render(request,'account/modifier_user.html',context) 
    # GET
    else:
        return render(request,'account/modifier_user.html', {'user':user,'countries': countries})   