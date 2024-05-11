from django.db import models
from django.core.exceptions import ValidationError
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator 
from DIC1Shop.settings import AUTH_USER_MODEL
import uuid
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
    class Meta:
        verbose_name = 'Produit'
    nom = models.CharField(max_length = 128)
    description = models.TextField(blank=True)
    marque = models.CharField(max_length=128)
    ref = models.CharField(max_length=128,unique=True)
    prix = models.FloatField()
    stock = models.IntegerField(verbose_name = 'Quantité disponible', default = 0,validators=[MinValueValidator(0)])
    categorie = models.ForeignKey(Categorie, on_delete = models.SET_NULL, null = True, blank = True)
    slug = models.SlugField(max_length = 128,blank=True,unique=True)
    star = models.IntegerField(default=0 ,verbose_name = 'notes',blank=True,validators=[MinValueValidator(1), MaxValueValidator(5)])
    
    def __str__(self):
        return self.nom
    
    def save(self, *args, **kwargs):
        if not self.slug:
            uuid_code = str(uuid.uuid4().hex)[:6] 
            base_slug = slugify(self.nom)
            self.slug = f"{base_slug}-{uuid_code}"
        super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse('single-product-view', kwargs={'slug': self.slug})
    
class ImageProduit(models.Model):
    class Meta:
        verbose_name = 'images'
    produit = models.ForeignKey(Produit, related_name='images', on_delete=models.CASCADE)
    nom = models.CharField(max_length = 128)
    image = models.ImageField(upload_to='images_prod')

    def __str__(self):
        return self.nom
class Article(models.Model):
    class Meta:
        verbose_name = 'Article'
    user = models.ForeignKey(AUTH_USER_MODEL,on_delete = models.CASCADE)
    quantite = models.IntegerField(default = 1, verbose_name = "Nombre d'article",validators=[MinValueValidator(1)])
    produit = models.ForeignKey(Produit, on_delete = models.CASCADE) # un produit peut appartenir à +sieurs article
    statutCommande = models.BooleanField(default = False)
    dateCommande = models.DateTimeField(blank = True, null = True)
    def __str__(self) -> str:
        return f"{self.produit.nom} ({self.quantite})"
    
    @property
    def prix_total(self):
        total = self.quantite * self.produit.prix
        return total  
    
    def clean(self):
        super().clean()
        if self.quantite > self.produit.stock:
            raise ValidationError("La quantité ne peut pas dépasser le stock disponible du produit.")         

class Panier(models.Model):
    class Meta:
        verbose_name = 'Panier'
    # user = models.ForeignKey(unique = True,AUTH_USER_MODEL, on_delete = models.CASCADE)
    # équivalent à 
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete = models.CASCADE)
    articles = models.ManyToManyField(Article,blank=True)
    taxes = models.FloatField(default=0.0,blank = True)
    frais = models.FloatField(default=0.0, blank = True)
    def get_montant(self):
        return sum(article.prix_total for article in self.articles.all())

    @property
    def montant(self):
        return self.get_montant()
    
    @property
    def montantTotal(self):
        return self.get_montant() + self.taxes + self.frais

    @property 
    def quantitePanier(self):
        cartitems = self.articles.all()
        total = sum([item.quantite for item in cartitems])
        return total
    
    def __str__(self):
        return f"{self.user.prenom} {self.user.nom}"
