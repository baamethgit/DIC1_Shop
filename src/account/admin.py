from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import UserModel
from django.contrib.auth.models import Group

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = UserModel
    list_display = ("courriel", "is_active",)
    list_filter = ("is_active",)
    search_fields = ("courriel",)
    ordering = ("courriel",)
    filter_horizontal = []  # Supprime les champs groups et user_permissions de la configuration
    fieldsets = (
        (None, {"fields": ("courriel", "password")}),
        ("Informations personnelles", {"fields": ("prenom","nom","date_naissance","mail_secondaire","adresse","telephone","pays","region" ,"code_postal" )}),
        ("Permissions", {"fields": ("is_active",)}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "courriel", "prenom", "nom", "date_naissance", "password1", "password2", "is_staff",
                "is_active",
            )
        }),
    )


# Register your models here.
admin.site.register(UserModel, CustomUserAdmin)
admin.site.unregister(Group)