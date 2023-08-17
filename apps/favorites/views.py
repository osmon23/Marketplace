from django.shortcuts import get_object_or_404
from rest_framework import permissions, status, generics
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .models import Favorite, FavoriteItem
from .serializers import FavoriteItemListSerializer, FavoriteItemSerializer

from ..stores.models import Product


class AddToFavoriteView(generics.CreateAPIView):
    serializer_class = FavoriteItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        product_id = self.request.data.get('product_id')

        try:
            favorite = Favorite.objects.get(customer=user)
        except Favorite.DoesNotExist:
            favorite = Favorite.objects.create(customer=user)

        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            raise ValidationError({"detail": "Product not found."})

        favorite_item, created = FavoriteItem.objects.get_or_create(favorite=favorite, product=product)
        favorite_item.save()

        serializer = self.serializer_class(favorite_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        return FavoriteItem.objects.all


class RemoveFromFavoriteView(generics.DestroyAPIView):
    serializer_class = FavoriteItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return FavoriteItem.objects.filter(favorite__customer=user)

    def perform_destroy(self, instance):
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self):
        queryset = self.get_queryset()
        filter_kwargs = {
            'favorite__customer': self.request.user,
            'product_id': self.kwargs['pk']
        }
        obj = get_object_or_404(queryset, **filter_kwargs)
        return obj


class FavoriteItemsListView(generics.ListAPIView):
    serializer_class = FavoriteItemListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        try:
            favorite = Favorite.objects.get(customer=user)
            return favorite.favorite_items.all()
        except Favorite.DoesNotExist:
            return []

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)