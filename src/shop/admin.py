from django.contrib import admin

from .models import Produit,ImageProduit

# Register your models here.
admin.site.register(Produit)
admin.site.register(ImageProduit)