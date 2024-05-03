from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView

from DIC1Shop.settings import AUTH_USER_MODEL
from .models import Produit,Categorie,Panier,Article
from django.views import defaults as default_views
from django.contrib.auth import get_user_model
from django.http import JsonResponse

User = get_user_model()

# Create your views here.
class detailProduit(DetailView):
    pass

def listProduit(request):
    produits = Produit.objects.all()
    categories = Categorie.objects.all()
    return render(request,'shop/liste_produits.html', {'produits':produits,'categories':categories})

def detailProduit(request,slug):
    produit = Produit.objects.all().filter(slug = slug).last()
    return render(request,'shop/detail_produit.html', {'produit':produit})


def produitParCategorie(request,slug):
    try:
        categorie = Categorie.objects.all().get(slug = slug)
        produits = categorie.produit_set.all()
    except:
        return render(request,'shop/list_par_categorie.html')
    return render(request,'shop/list_par_categorie.html', {'produits':produits})

def panier(request):
    user=request.user
    panier = get_object_or_404(Panier,user = user)
    articles = panier.articles.all()
    return render(request,'shop/panier.html' ,{'articles':articles,'panier':panier})

def ajouter_prod_au_panier(request):
    return render(request,'j.html')