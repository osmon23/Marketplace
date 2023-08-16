from rest_framework import serializers
from .models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = ('id', 'product_id', 'quantity')


class CartItemListSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()

    class Meta:
        model = CartItem
        fields = ('product', 'quantity')