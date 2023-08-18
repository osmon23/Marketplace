from rest_framework import viewsets, permissions, generics

from .models import Product, Store, Review, Category, ProductDiscount
from .serializers import (
    ProductSerializer,
    StoreSerializer,
    ReviewCreateSerializer,
    CategorySerializer,
    ProductDiscountSerializer
)
from .permissions import IsAdminOrSeller


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [permissions.AllowAny]


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
    permission_classes = [permissions.AllowAny]
