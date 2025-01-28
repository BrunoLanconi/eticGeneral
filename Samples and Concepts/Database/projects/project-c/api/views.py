from rest_framework.viewsets import ModelViewSet

from api.models import Product
from api.serializers import ProductSerializer

class ProductsViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
  
    