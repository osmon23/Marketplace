from rest_framework import viewsets, permissions, status, request, generics
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from ..stores.models import Product


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user.customer)

    def perform_update(self, serializer):
        instance = self.get_object()

        if instance.customer != self.request.user.customer:
            return Response(
                {"detail": "You don't have permission to update this cart."},
                status=status.HTTP_403_FORBIDDEN
            )
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.customer != self.request.user.customer:
            return Response(
                {"detail": "You don't have permission to delete this cart."},
                status=status.HTTP_403_FORBIDDEN
            )

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


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