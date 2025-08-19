import django_filters
from .models import Product, Brand, Category


class ProductFilter(django_filters.FilterSet):
    # диапазон цены
    min_price = django_filters.NumberFilter(field_name="new_price", lookup_expr="gte")
    max_price = django_filters.NumberFilter(field_name="new_price", lookup_expr="lte")

    class Meta:
        model = Product
        fields = {
            'category': ['exact'],   # фильтр по категории
            'brands': ['exact'],     # фильтр по бренду
            'is_active': ['exact'],  # активные/неактивные
        }
