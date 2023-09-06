from django.db.models import Q
from django_filters import rest_framework as django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_search')
    category = django_filters.CharFilter(method='category_search')
    address = django_filters.CharFilter(method='address_search')
    country = django_filters.CharFilter(method='country_search')
    brand = django_filters.CharFilter(method='brand_search')
    fuel = django_filters.CharFilter(method='fuel_search')
    price__gte = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price__lte = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = []

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

    def country_search(self, queryset, country_of_origin, value):
        if value:
            queryset = queryset.filter(
                Q(country_of_origin__icontains=value) |
                Q(country_of_origin__icontains=value.capitalize())
            )
        return queryset

    def brand_search(self, queryset, brand, value):
        if value:
            queryset = queryset.filter(
                Q(brand__icontains=value) |
                Q(brand__icontains=value.capitalize())
            )
        return queryset

    def fuel_search(self, queryset, name, value):
        if value:
            queryset = queryset.filter(
                Q(fuel_type__name__icontains=value) |
                Q(fuel_type__name__icontains=value.capitalize())
            )
        return queryset








