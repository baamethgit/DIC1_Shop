from django.db import models
from django.template.defaultfilters import slugify

class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    slug = models.SlugField(max_length = 128,blank = True)
    
    def __str__(self):
        return self.nom
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.nom)
        super().save(*args,**kwargs)
        
class Produit(models.Model):
    nom = models.CharField(max_length = 128)
    description = models.TextField()
    marque = models.CharField(max_length=128)
    reference = models.CharField(max_length=128)
    prix = models.FloatField()
    stock = models.IntegerField(verbose_name = 'Quantité disponible', default = 0)
    categorie = models.ForeignKey(Categorie, on_delete = models.SET_NULL, null = True, blank = True)
    slug = models.SlugField(max_length = 128,blank=True)
    
    def __str__(self):
        return self.nom
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.nom)
        super().save(*args,**kwargs)

class ImageProduit(models.Model):
    produit = models.ForeignKey(Produit, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images_prod')

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
    