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
        user.is_admin = True
        user.save(using=self._db)
        return user
    
# Modele utilisateur
class UserModel(AbstractBaseUser):
    prenom = models.CharField(max_length=128)
    nom = models.CharField(max_length=128)
    date_naissance = models.DateField(verbose_name='Date de naissance')
    courriel = models.EmailField(unique = True)
    mail_secondaire = models.EmailField(blank=True, null=True,unique = True)
    telephone = models.CharField(max_length=128,blank=True, null=True)
    adresse = models.CharField(max_length = 250,blank=True, null=True)
    pays = models.CharField(max_length=128,blank=True, null=True)
    region = models.CharField(max_length=128,blank=True, null=True)
    code_postal = models.CharField(max_length=128,blank=True, null=True)
    
    REQUIRED_FIELDS = ['prenom', 'nom', 'date_naissance']
    USERNAME_FIELD = 'courriel'
    EMAIL_FIELD = 'courriel'
    
    objects = UserManager()

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    def __str__(self):
        return self.courriel

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True