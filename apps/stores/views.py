from rest_framework import viewsets, permissions, generics, status
from rest_framework import filters
from django_filters import rest_framework as django_filters
from rest_framework.response import Response


from .filters import ProductFilter
from .models import Product, Store, Review, Category, ProductDiscount
from .serializers import (
    ProductSerializer,
    StoreSerializer,
    ReviewCreateSerializer,
    CategorySerializer,
    ProductDiscountSerializer
)
from apps.stores.permissions import IsAdminOrSeller


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-range_weight')
    serializer_class = ProductSerializer
    filter_backends = [filters.OrderingFilter, django_filters.DjangoFilterBackend]
    filterset_class = ProductFilter
    ordering_fields = ['name', 'price']
    permission_classes = [IsAdminOrSeller]

    def perform_create(self, serializer):
        seller = self.request.user
        product_limit = seller.store.product_limit

        if seller.products.count() >= product_limit:
            return Response({'error': 'Превышен лимит продуктов для этого продавца.'},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer.save(store=seller.store)


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsAdminOrSeller]


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
    permission_classes = [IsAdminOrSeller]

