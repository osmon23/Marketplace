from django.contrib import admin

from apps.cart.models import Cart, CartItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer',)
    list_display_links = ('id', 'customer',)


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'product', 'quantity')
    list_display_links = ('id', 'cart', 'product')