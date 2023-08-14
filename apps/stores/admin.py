from django.contrib import admin
from .models import Specifications, ProductImage, Product, Store, Review


class SpecificationsInline(admin.TabularInline):
    model = Specifications
    extra = 1


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1
    readonly_fields = (
        "name",
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        SpecificationsInline,
        ProductImageInline,
        ReviewInline,
    ]
    save_on_top = True
    list_display = (
        'id',
        'name',
        'price',
        'quantity',
    )
    list_display_links = (
        'name',
    )


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'address',
    )
    list_display_links = (
        'name',
    )
    search_fields = (
        'name',
        'address',
    )


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
    )
    list_display_links = (
        'id',
    )


@admin.register(Specifications)
class SpecificationsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )
    list_display_links = (
        'id',
        'name',
    )
    search_fields = (
        'name',
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "parent",
        "product",
        "id"
    )
    readonly_fields = (
        "name",
    )