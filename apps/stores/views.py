from rest_framework import viewsets, permissions, generics
from rest_framework import filters

from django_filters import rest_framework as django_filters
from rest_framework.response import Response


from .filters import ProductFilter
from .models import (
    Product,
    Store,
    Review,
    Category,
    ProductDiscount,
)

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

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        products = Product.objects.filter(store=instance)
        store_serializer = StoreSerializer(instance)
        product_serializer = ProductSerializer(products, many=True)

        response_data = {
            "store_info": store_serializer.data,
            "products": product_serializer.data
        }
        return Response(response_data)


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

