import json
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Produit,Categorie,Panier,Article
from django.http import JsonResponse
from django.views.generic import ListView

def listProduit(request):
    produits = Produit.objects.all()
    categories = Categorie.objects.all()
    return render(request,'shop/liste_produits.html', {'produits':produits,'categories':categories,'display_search_bar':3})

# class listProduit(ListView):
#     model = Produit
#     context_object_name = "produits"  # Le nom de l'objet de contexte
#     template_name = "shop/liste_produits.html"  # Le nom du template
#     paginate_by = 2  # Nombre d'éléments par page


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
        if produit.stock == 0:
            erreur = f"Ce produit n'est plus disponible"
            return render(request,'shop/detail_produit.html', {'produit':produit,'erreur':erreur})
        if cree:
            article.quantite = int(quantite)
        else:
            article.quantite += int(quantite)
        if article.quantite > produit.stock:
            erreur = f'La quantité ne peut pas dépasser le stock disponible({produit.stock}).'
            return render(request,'shop/detail_produit.html', {'produit':produit,'erreur':erreur})
        article.save()
        panier.articles.add(article)
        panier.save()
        return redirect('cart-view')
    else:
        try:
            produit = Produit.objects.all().get(slug = slug)
        except:
            return render(request,'404.html', {'msg_page_not_found':'produit non retrouvé'})
        return render(request,'shop/detail_produit.html', {'produit':produit})

def rechercheProduit(request):
    query = request.GET.get('query_')
    categories = Categorie.objects.all()
    produits = Produit.objects.filter(nom__icontains=query)
    context = {'produits':produits,'categories':categories,'display_search_bar':3,'query':query}
    if not produits:
        context['search_failed'] = 2 
    return render(request,'shop/liste_produits.html', context)


def produitParCategorie(request,slug):
    try:
        categories = Categorie.objects.all()
        categorie = Categorie.objects.all().get(slug = slug)
        produits = categorie.produit_set.all()
    except:
        return render(request,'404.html', {'msg_page_not_found':"Cette catégorie n'existe pas"})
    context = {'categories':categories,'categorie':categorie,'produits':produits,'checked_btn':categorie.slug,'display_search_bar':3}
    return render(request,'shop/list_par_categorie.html', context = context)

def panier(request):
    user=request.user
    if not user.is_authenticated:
        return redirect('signup-login-view')
    panier = get_object_or_404(Panier,user = user)
    articles = panier.articles.all()
    return render(request,'shop/panier.html' ,{'articles':articles,'panier':panier})

def updateQuantity(request):
    data = json.loads(request.body)
    inputval = int(data['in_val'])
    id_produit = data['p_id']
    
    if request.user.is_authenticated:
        user = request.user
        produit = get_object_or_404(Produit, pk=int(id_produit))
        panier, created = Panier.objects.get_or_create(user = user)
        article, created = Article.objects.get_or_create(produit=produit, user = user)

        article.quantite = inputval
        article.save()

        msg = {
            'prix_total_article':article.prix_total,
            'montant': panier.montant,
            'montant_total': panier.montantTotal,
            'quantite_panier': panier.quantitePanier
        }
    return JsonResponse(msg, safe=False)


def validerPanier(request):
    panier = Panier.objects.all().get(user = request.user)
    if request.method == 'POST': 
        if panier.articles.exists():
            for article in panier.articles.all():
                if article.quantite > article.produit.stock:
                    erreur = f"La quantité de {article.produit.nom} dépasse le stock disponible ({article.produit.stock})."
                    url = reverse('cart-view') + f'?erreur={erreur}'
                    return redirect(url)
            for article in panier.articles.all():
                article.produit.stock -= int(article.quantite)
                article.produit.save()
            return render(request,'shop/validation_panier.html')
        else:
            return render(request,'shop/panier.html' ,{'panier':panier,"erreur":'Votre panier est Vide .'})
    return redirect('cart-view')

def supprimerArticleDuPanier(request):
    data = json.loads(request.body)
    id_article = data['a_id']
    if request.user.is_authenticated:
        user = request.user
        article = Article.objects.get(pk = int(id_article))
        panier = Panier.objects.all().get(user = user)
        panier.articles.remove(article)
        article.delete()
        panier.save()
        msg = {
            'montant': panier.montant,
            'montant_total': panier.montantTotal,
            'quantite_panier': panier.quantitePanier
        }
    return JsonResponse(msg, safe=False)