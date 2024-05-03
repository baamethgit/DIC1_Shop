from django.urls import path
from django.views.generic import TemplateView
from .views import listProduit,detailProduit,produitParCategorie,panier,updateQuantity,ajouter_prod_au_panier
from django.conf.urls.static import static
# from  DIC1Shop.settings import MEDIA_ROOT,MEDIA_URL

urlpatterns = [
    path('panier/', panier, name='cart-view'),
    path('produits/all',listProduit,name='all-product-view'),
    path('produits/categories/<str:slug>',produitParCategorie,name='categorie-view'),
    path("produit/<str:slug>", detailProduit, name='single-product-view'),
    # path('updatecart/', updateCart),:
    path('updatequantity/', updateQuantity),
    ] 
# + static(MEDIA_URL,document_root = MEDIA_ROOT)
