from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

from DIC1Shop.settings import AUTH_USER_MODEL

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
        
    def get_absolute_url(self):
        return reverse("home-view")
class ImageProduit(models.Model):
    produit = models.ForeignKey(Produit, related_name='images', on_delete=models.CASCADE)
    nom = models.CharField(max_length = 128)
    image = models.ImageField(upload_to='images_prod')

    def __str__(self):
        return self.nom
class Article(models.Model):
    STATUS_CHOICES = (
    ('en_attente', 'En attente de traitement'),
    ('en_cours', 'En cours de livraison'),
    ('livre', 'Livré'),
    )
    user = models.ForeignKey(AUTH_USER_MODEL,on_delete = models.CASCADE)
    quantite = models.IntegerField(default = 1, verbose_name = "Nombre d'article")
    produit = models.ForeignKey(Produit, on_delete = models.CASCADE) # un produit peut appartenir à +sieurs article
    statusCommande = models.CharField(max_length=100,choices=STATUS_CHOICES)
    def __str__(self) -> str:
        return f"{self.produit.nom} ({self.quantite})"
    
class Panier(models.Model):
    STATUS_CHOICES = (
    ('en_attente', 'En attente de traitement'),
    ('en_cours', 'En cours de livraison'),
    ('livre', 'Livré'),
    )
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete = models.CASCADE)
    articles = models.ManyToManyField(Article)
    
    def get_total_amount(self):
        return sum(article.produit.prix * article.quantite for article in self.articles.all())

    @property
    def montant(self):
        return self.get_total_amount()
    status = models.CharField(max_length=100,choices=STATUS_CHOICES)
    dateCommande = models.DateTimeField(blank = True, null = True)
