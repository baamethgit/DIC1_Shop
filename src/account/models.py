from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
class UserManager(BaseUserManager):    
    def create_user(self, courriel,prenom, nom, date_naissance, password=None):
        if not courriel:
            raise ValueError("L\'adresse courriel doit être fournie'")
        user = self.model(
            courriel=self.normalize_email(courriel),
            prenom = prenom,
            nom = nom,
            date_naissance=date_naissance,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, courriel,prenom, nom, date_naissance, password=None):
        user = self.create_user(
            courriel = courriel,
            prenom = prenom,
            nom = nom,
            date_naissance=date_naissance,
            password=password,
        )
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user
    
# Modele utilisateur
class UserModel(AbstractBaseUser):
    prenom = models.CharField(max_length=128)
    nom = models.CharField(max_length=128)
    date_naissance = models.DateField(verbose_name='Date de naissance')
    courriel = models.EmailField(unique = True,max_length = 255)
    mail_secondaire = models.EmailField(blank=True, null=True,unique = True , verbose_name='Email Secondaire')
    telephone = models.CharField(max_length=128,blank=True, null=True,verbose_name = "Numéro de téléphone")
    adresse = models.CharField(max_length = 250,blank=True, null=True,verbose_name='Adresse')
    pays = models.CharField(max_length=128,blank=True, null=True,verbose_name='Pays')
    region = models.CharField(max_length=128,blank=True, null=True,verbose_name='Région')
    code_postal = models.CharField(max_length=128,blank=True, null=True,verbose_name='Code Postal')
    
    REQUIRED_FIELDS = ['prenom', 'nom', 'date_naissance']
    USERNAME_FIELD = 'courriel'
    EMAIL_FIELD = 'courriel'
    
    objects = UserManager()
    
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    def __str__(self):
        return self.courriel

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True
    
# Ce code est basé sur les exemples donnée dans la documentation de django 4.2