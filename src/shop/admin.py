from django.contrib import admin

from .models import Produit,ImageProduit,Categorie,Panier,Article

class produitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix', 'stock','star','marque')
    list_filter = ('stock',)
    search_fields = ('nom',)

class articleAdmin(admin.ModelAdmin):
    list_display = ('produit', 'user', 'quantite','prix_total')
    list_filter = ('quantite',)
    search_fields = ('produit',)

class panierAdmin(admin.ModelAdmin):
    list_display = ('user', 'montantTotal', 'frais','taxes','quantitePanier')
    search_fields = ('user',)

admin.site.register(Categorie)
admin.site.register(Produit,produitAdmin)
admin.site.register(ImageProduit)
admin.site.register(Article,articleAdmin)
admin.site.register(Panier,panierAdmin)
