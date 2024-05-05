import json
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Produit,Categorie,Panier,Article
from django.http import JsonResponse


def listProduit(request):
    produits = Produit.objects.all()
    categories = Categorie.objects.all()
    return render(request,'shop/liste_produits.html', {'produits':produits,'categories':categories})

def detailProduit(request,slug):
    if request.method == 'POST':    
        user=request.user
        if not user.is_authenticated:
            return redirect('signup-login-view')
        id = request.POST.get('id_produit')
        quantite = request.POST.get('quantite')
        produit = Produit.objects.get(pk=id)
        panier_existe = Panier.objects.filter(user=user).exists()
        if not panier_existe:
            panier = Panier.objects.create(user=user)
        else:
            panier = Panier.objects.get(user=user)
            
        article,cree = Article.objects.get_or_create(user = user,produit = produit)
        if cree:
            article.quantite = int(quantite)
        else:
            article.quantite += int(quantite)
        article.save()
        panier.articles.add(article)
        panier.save()
        return redirect('cart-view')
    else:
        try:
            produit = Produit.objects.all().get(slug = slug)
        except:
            return render(request,'shop/page_404.html', {'erreur':'produit non retrouvé'})
        return render(request,'shop/detail_produit.html', {'produit':produit})


def produitParCategorie(request,slug):
    try:
        categorie = Categorie.objects.all().get(slug = slug)
        produits = categorie.produit_set.all()
    except:
        return render(request,'shop/page_404.html', {'erreur':"Cette catégorie n'existe pas"})
    return render(request,'shop/list_par_categorie.html', {'produits':produits})

def panier(request):
    user=request.user
    if not user.is_authenticated:
        return redirect('signup-login-view')
    panier = get_object_or_404(Panier,user = user)
    articles = panier.articles.all()
    if request == "POST":
        request.POST.get("a")
        
    return render(request,'shop/panier.html' ,{'articles':articles,'panier':panier})

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


def validerPanier(request):
    return render(request,'shop/validation_panier.html')