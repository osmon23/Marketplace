from rest_framework import viewsets, permissions, generics
from rest_framework import filters

from django_filters import rest_framework as django_filters

from .filters import ProductFilter
from .models import Product, Store, Review, Category, ProductDiscount
from .serializers import (
    ProductSerializer,
    StoreSerializer,
    ReviewCreateSerializer,
    CategorySerializer,
    ProductDiscountSerializer
)
from .permissions import IsAdminOrSellerOrReadOnly


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-range_weight')
    serializer_class = ProductSerializer
    filter_backends = [filters.OrderingFilter, django_filters.DjangoFilterBackend]
    filterset_class = ProductFilter
    ordering_fields = ['name', 'price']
    permission_classes = [IsAdminOrSellerOrReadOnly]


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsAdminOrSellerOrReadOnly]


class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewCreateSerializer
    queryset = Review.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]


class ProductDiscountViewSet(viewsets.ModelViewSet):
    queryset = ProductDiscount.objects.all()
    serializer_class = ProductDiscountSerializer
    permission_classes = [IsAdminOrSellerOrReadOnly]

