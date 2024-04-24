from django.shortcuts import render
from django.views.generic import DetailView
from .models import Produit
from django.views import defaults as default_views
# /mport http404
# Create your views here.
class detailProduit(DetailView):
    pass

def listProduit(request):
    produits = Produit.objects.all()
    return render(request,'list.html', {'produits':produits})

def detailProduit(request,slug):
    try:
        produit = Produit.objects.all().get(slug = slug)
    except:
        return default_views.page_not_found()
    return render(request,'detail.html', {'produit':produit})