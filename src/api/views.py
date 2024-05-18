from shop.models import Produit,Categorie,ImageProduit

from .serializers import ProductSerializer,CategorySerializer
from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework.response import Response


class listProduits(ListAPIView):
    queryset = Produit.objects.all()
    serializer_class = ProductSerializer
    
class ProduitsParCategorie(ListAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        category = Categorie.objects.get(slug = category_slug)
        return Produit.objects.filter(categorie=category)

class CategoryList(ListAPIView):
    queryset = Categorie.objects.all()
    serializer_class = CategorySerializer
    
class ProduitDetail(RetrieveAPIView):
    queryset = Produit.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    
