from django.contrib import admin

from .models import Favorite, FavoriteItem


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer',)
    list_display_links = ('id', 'customer',)


@admin.register(FavoriteItem)
class FavoriteItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'favorite', 'product')
    list_display_links = ('id', 'favorite', 'product')
