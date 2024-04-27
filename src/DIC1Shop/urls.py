"""
URL configuration for DIC1Shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from DIC1Shop.views import home
from django.views.generic import TemplateView
from django.conf.urls.static import static
from .settings import MEDIA_ROOT,MEDIA_URL
from shop.views import listProduit,detailProduit,produitParCategorie

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',home,name = 'home-view'),
    path("account/",include("account.urls")),
    path("shop/panier", TemplateView.as_view(template_name = 'shop/panier.html'), name='cart_view'),
    path("shop/detail_produit", TemplateView.as_view(template_name = 'shop/detail_produit.html'), name='prod_view'),
    path('liste',listProduit),
    path('detail/<str:slug>',detailProduit),
    path('prod_par_categorie/<str:slug>',produitParCategorie),
]+ static(MEDIA_URL,document_root = MEDIA_ROOT)