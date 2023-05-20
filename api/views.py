from shop.models import Product
from .serializers import ProductSerializer
from rest_framework import viewsets
from .permissions import IsAdminOrReadOnly
from .filters import ProductFilter


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    lookup_field = 'slug'
