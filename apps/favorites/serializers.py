from rest_framework import serializers
from .models import FavoriteItem


class FavoriteItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = FavoriteItem
        fields = ('id', 'product_id',)


class FavoriteItemListSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()

    class Meta:
        model = FavoriteItem
        fields = ('product',)