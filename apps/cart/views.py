from rest_framework import permissions, status, generics
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import Cart, CartItem
from .serializers import CartItemSerializer, CartItemListSerializer
from ..stores.models import Product


class AddToCartView(generics.CreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        product_id = self.request.data.get('product_id')
        quantity = int(self.request.data.get('quantity', 1))

        try:
            cart = Cart.objects.get(customer=user)
        except Cart.DoesNotExist:
            cart = Cart.objects.create(customer=user)

        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            raise ValidationError({"detail": "Product not found."})

        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        cart_item.quantity += quantity
        cart_item.save()

        serializer = self.serializer_class(cart_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        return CartItem.objects.all


class RemoveFromCartView(generics.DestroyAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return CartItem.objects.filter(cart__customer=user)

    def perform_destroy(self, instance):
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self):
        queryset = self.get_queryset()
        filter_kwargs = {
            'cart__customer': self.request.user,
            'product_id': self.kwargs['pk']
        }
        obj = get_object_or_404(queryset, **filter_kwargs)
        return obj


class CartItemsListView(generics.ListAPIView):
    serializer_class = CartItemListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        try:
            cart = Cart.objects.get(customer=user)
            return cart.cart_items.all()
        except Cart.DoesNotExist:
            return []

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

####### dgsdhdh