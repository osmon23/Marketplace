from rest_framework import serializers
from .models import CartItem


class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = ('id', 'product_id', 'quantity')


class CartItemListSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(source='product.id')
    product = serializers.StringRelatedField()

    class Meta:
        model = CartItem
        fields = ('product', 'product_id', 'quantity')