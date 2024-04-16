from django.db import models

class Produit(models.Model):
    nom = models.CharField(max_length = 128)
    marque = models.CharField(max_length = 128)
    description = models.TextField()
    reference = models.CharField(max_length = 128)
    image = models.ImageField(upload_to = 'images/produits', verbose_name = 'Illustration')
    prix = models.FloatField()
    stock = models.IntegerField(verbose_name = 'Quantité disponible', default = 0)
    categorie = models.CharField(max_length = 128)

# class Article(models.Model):
#     # user = models.ForeignKey(AUTH_USER_MODEL)
#     quantite = models.IntegerField(default = 1, verbose_name = "Nombre d'article")
#     produit = models.ForeignKey(Produit, on_delete = models.CASCADE) # un produit peut appartenir à +sieurs article
#     statusCommande = models.BooleanField(default = False)
#     couleur = models.CharField(max_length = 128)
    
#     def __str__(self) -> str:
#         return f"{self.produit.nom} ({self.quantite})"
    
# class Panier(models.Model):
#     # user = models.OneToOneField(AUTH_USER_MODEL, on_delete = models.CASCADE) 
#     # un utilisateur ne peut avoir qu'un seul panier (<=> à foreignKey avec unique=True)
#     articles = models.ManyToManyField(Article)
#     montant = models.FloatField()
#     statusCommande = models.BooleanField(default = False)
#     dateCommande = models.DateTimeField(blank = True, null = True)
    