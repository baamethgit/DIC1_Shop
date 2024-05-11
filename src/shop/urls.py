from django.urls import path
from .views import rechercheProduit,detailProduit,produitParCategorie,panier,updateQuantity,validerPanier,supprimerArticleDuPanier
from django.views.generic import TemplateView
urlpatterns = [
    path('panier/', panier, name='cart-view'),
    path('valider_panier/',validerPanier,name='valid-panier'),
    path('produits/categories/<str:slug>',produitParCategorie,name='categorie-view'),
    path("produit/<str:slug>", detailProduit, name='single-product-view'),
    path('updatequantity/', updateQuantity),
    path('panier/supprimer_article/', supprimerArticleDuPanier),
    path('produits/recherche/',rechercheProduit,name='search-view'),
    path('<str:blabla>/',TemplateView.as_view(template_name= '404.html'))
    ]