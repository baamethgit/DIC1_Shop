from django.urls import path
from .views import ProduitsParCategorie, listProduits,CategoryList,ProduitDetail

urlpatterns = [
    path("products/all/",listProduits.as_view()),
    path("product/<str:slug>/",ProduitDetail.as_view()),
    path("categories/all/",CategoryList.as_view()),
    path('products/categories/<slug:category_slug>/',ProduitsParCategorie.as_view()),
    
]