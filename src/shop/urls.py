from django.urls import path
from django.views.generic import TemplateView
from .views import listProduit,detailProduit,produitParCategorie,panier,updateQuantity,validerPanier

urlpatterns = [
    path('panier/', panier, name='cart-view'),
    path('valider_panier/',validerPanier,name='valid-panier'),
    # path('produits/all',listProduit,name='all-product-view'),
    path('produits/categories/<str:slug>',produitParCategorie,name='categorie-view'),
    path("produit/<str:slug>", detailProduit, name='single-product-view'),
    path('updatequantity/', updateQuantity),
    ] 