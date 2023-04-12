from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers
from shop.models import Product


class ProductSerializer(FlexFieldsModelSerializer,
                        serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'slug', 'fullname', 'sku', 'image',
                  'description', 'price', 'available', 'description')
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
