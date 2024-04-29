from django.shortcuts import render
from django.views.generic import DetailView
from .models import Produit,Categorie
from django.views import defaults as default_views

# Create your views here.
class detailProduit(DetailView):
    pass

def listProduit(request):
    produits = Produit.objects.all()
    categories = Categorie.objects.all()
    return render(request,'liste_produits.html', {'produits':produits,'categories':categories})

def detailProduit(request,slug):
    try:
        produit = Produit.objects.all().get(slug = slug)
    except:
        return default_views.page_not_found()
    return render(request,'detail.html', {'produit':produit})


def produitParCategorie(request,slug):
    try:
        categorie = Categorie.objects.all().get(slug = slug)
        produits = categorie.produit_set.all()
    except:
        return default_views.page_not_found()
    return render(request,'list_par_categorie.html', {'produits':produits})