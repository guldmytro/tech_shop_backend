from shop.models import Product
from .serializers import ProductSerializer
from rest_framework import viewsets
from .permissions import IsAdminOrReadOnly


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
