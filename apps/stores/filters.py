from django.db.models import Q
from django_filters import rest_framework as django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_search')
    category = django_filters.CharFilter(method='category_search')
    address = django_filters.CharFilter(method='address_search')
    price__gte = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price__lte = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = [
            'name',
            'category',
            'address'
        ]

    def filter_search(self, queryset, name, value):
        if value:
            queryset = queryset.filter(
                Q(name__icontains=value) |
                Q(name__icontains=value.capitalize())
            )
        return queryset

    def category_search(self, queryset, category, value):
        if value:
            queryset = queryset.filter(
                Q(category__name__icontains=value) |
                Q(category__name__icontains=value.capitalize())
            )
        return queryset

    def address_search(self, queryset, address, value):
        if value:
            queryset = queryset.filter(
                Q(store__address__icontains=value) |
                Q(store__address__icontains=value.capitalize())
            )
        return queryset





