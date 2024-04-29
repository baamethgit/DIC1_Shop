from django.contrib import admin

from .models import Produit,ImageProduit,Categorie,Panier,Article

# Register your models here.
admin.site.register(Categorie)
admin.site.register(Produit)
admin.site.register(ImageProduit)
admin.site.register(Article)
admin.site.register(Panier)
