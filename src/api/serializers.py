from rest_framework.serializers import ModelSerializer
from shop.models import Produit,Categorie,ImageProduit

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'


class ImageProduitSerializer(ModelSerializer):
    class Meta:
        model = ImageProduit
        fields = ['nom', 'image']
        
class ProductSerializer(ModelSerializer):
    categorie = CategorySerializer()  # serializer imbriqué
    images = ImageProduitSerializer(many=True, read_only=True)
    class Meta:
        model = Produit
        fields = "__all__"
        extra_kwargs = {
            'images': {'source': 'imageproduit_set'}  # Ajoute le champ images
        }