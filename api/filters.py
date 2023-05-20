import django_filters
from shop.models import Product


class ProductFilter(django_filters.FilterSet):
    id = django_filters.CharFilter(field_name='id', method='filter_by_id')

    def filter_by_id(self, queryset, field_name, value):
        if value:
            ids = value.split(',')
            return queryset.filter(id__in=ids)
        return queryset

    class Meta:
        model = Product
        fields = ['id', 'name', 'slug']
