import json
from django.shortcuts import get_object_or_404, redirect, render
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
    if request.method == 'POST':
        id = request.POST.get('id_produit')
        produit = Produit.objects.get(pk=id)
        user=request.user
        panier = get_object_or_404(Panier,user = user)
        article,cree = Article.objects.get_or_create(user = user,produit = produit)
        if cree:
            panier.articles.add(article)
            panier.save()
        else:
            article.quantite += 1
            article.save()
        return redirect('cart-view')
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
    if request == "POST":
        request.POST.get("a")
        
    return render(request,'shop/panier.html' ,{'articles':articles,'panier':panier})

# def updateCart(request):
#     data = json.loads(request.body)
#     product_id = data['product_id']
#     action = data['action']
#     if request.user.is_authenticated:
#         user = request.user
#         produit = Produit.objects.get(id= product_id)
#         panier, created = Panier.objects.get_or_create(user = user)
#         article, created = Article.objects.get_or_create(produit=produit, user = user)

#         if action == 'add':
#             article.quantite += 1
#         article.save()

#         msg = {
#             'quantite': panier.quantitePanier,
#             '':'',
#         }

#     return JsonResponse(msg, safe=False)

def updateQuantity(request):
    data = json.loads(request.body)
    inputval = int(data['in_val'])
    product_id = data['p_id']
    
    if request.user.is_authenticated:
        user = request.user
        produit = get_object_or_404(Produit, pk=int(product_id))
        panier, created = Panier.objects.get_or_create(user = user)
        article, created = Article.objects.get_or_create(produit=produit, user = user)

        article.quantite = inputval
        article.save()

        msg = {
            'prix_total':article.prix_total,
            'montant': panier.montant,
            'quantite_panier': panier.quantitePanier
        }
    return JsonResponse(msg, safe=False)






def ajouter_prod_au_panier(request):
    return render(request,'j.html')

def validerPanier(request):
    return render(request,'shop/validation_panier.html')