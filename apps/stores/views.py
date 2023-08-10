from rest_framework import viewsets

from .models import Product, Store
from .serializers import ProductSerializer, StoreSerializer
from .permissions import IsAdminOrSeller


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrSeller]


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsAdminOrSeller]

